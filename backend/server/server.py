from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from backend.server.ingest import save_only
from backend.server.generate import answer 
from backend.server.retrieval import hybrid
from backend.server.core.config import cfg
from backend.server import orchestrator
from pathlib import Path

'''loads environment variables from .env file'''
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))
app = Flask (__name__)
'''CORS is needed when Flask application is hosted on different domain'''
CORS(app)


def validate_upload_pdf(file_input):
    #require input file
    if file_input is None or file_input.filename.strip()=="":
        raise ValueError("Missing file")
    #check pdf header
    head = file_input.stream.read(5)
    file_input.stream.seek(0)
    if head != b"%PDF-":
        raise ValueError("Not a valid PDF (missing %PDF- header)")
    
    # tray parsing the pdf using pypdf
    try:
        reader = PdfReader(file_input.stream)
        _ = len(reader.pages)  

        file_input.stream.seek(0)
    
    except PdfReadError as e:
        file_input.stream.seek(0)
        raise ValueError(f"PDF parse error: {e}") from e
    except Exception as e:
        file_input.stream.seek(0)
        raise ValueError(f"PDF parse error: {type(e).__name__}: {e}") from e
def validate_query(user_query):
    #validate the JSON body for RAG queries

    if not isinstance(user_query, dict):
        raise ValueError("Invalid JSON body")
    prompt = str(user_query.get("prompt", "")).strip()
    if not prompt:
        raise ValueError ("Field prompt is required")
    top_k = user_query.get("top_k", 5)
    filters = user_query.get("filters") or None
    conversation_id = user_query.get("conversation_id")

    return prompt, top_k, filters, conversation_id

@app.post("/dev/summarize_hits")
def dev_summarize_hits():
    body = request.get_json(force=True, silent=False)

    question = str(body.get("prompt", "")).strip()
    hits = body.get("hits", [])
    if not question or not isinstance(hits, list):
        return jsonify({"error": "Provide 'prompt' and 'hits'[]"}), 400

    for i, h in enumerate(hits, start=1):
        # ensure required fields exist for _citations()
        h.setdefault("cite_id", i)
        h.setdefault("doc_id", f"dev-doc-{i}")
        h.setdefault("page", 1)
        h.setdefault("text", "")

    try:
        result = answer.synthesize_with_citations(question, hits)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "llm_error", "detail": str(e)}), 500
    

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/", methods = ["GET"])
def home():
    return jsonify(message="PLACEHOLDER_HOME")

@app.route("/chatbot", methods = ["GET"])
def chatbot():
    return jsonify(message="PLACEHOLDER_CHATBOT_FRONT_END")

@app.route("/ingest_document", methods = ["POST"])
def ingest_document():
    file = request.files.get("file")
    doc_id_from_client = request.form.get("doc_id")

    
    try:
        #validate pdf upload
        validate_upload_pdf(file)
        #pass document to ingestion pipeline
        ids = save_only.save_pdfs([file])
        if not ids:
            return jsonify({"error": "ingestion_failed", "detail": "No ID returned from save_pdfs"}), 500
        
        doc_id = ids[0]
        out_path = Path(cfg.DOC_STORE)/ f"{doc_id}.pdf"

        page_count =0
        try:
            with open(out_path, "rb") as fh:
                page_count = len(PdfReader(fh).pages)
        except Exception:
            pass

        return jsonify({
            "id": doc_id,
            "title": file.filename,
            "page_count": int(page_count),
            "chunk_count": 0
          
        }),201
    except ValueError as e:
        return jsonify({"error": "bad_request", "detail": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "ingestion_failed", "detail": str(e)}), 500

@app.post("/ingest_user_query")
def ingest_user_query():
    # 1) Parse and validate request body
    try:
        payload = request.get_json(force=True, silent=False)
        question, top_k, filters, conversation_id = validate_query(payload)
    except ValueError as e:
        return jsonify({"error": "bad_request", "detail": str(e)}), 400
    except Exception:
        return jsonify({"error": "bad_request", "detail": "Invalid JSON body"}), 400

    # 2) Run retrieval + LLM, with error handling
    try:
        # Retrieve from vector DB / hybrid search
        hits = hybrid.retrieve(question, top_k=top_k, filters=filters)

        for i, h in enumerate(hits, start=1):
            h.setdefault("cite_id", i)
            h.setdefault("title", h.get("doc_title") or h.get("filename") or "")
            h.setdefault("page", h.get("page") or 1)
            h.setdefault("text", h.get("text") or h.get("chunk") or "")
        #Ask watsonx.ai via orchestrator
        answer_text = orchestrator.synthesize(question, hits)

        return jsonify({
            "answer": answer_text,
            "citations": [
                {"cite_id": h["cite_id"], "title": h["title"], "page": h["page"]}
                for h in hits
            ],
            "retrieval": {
                "top_k": top_k,
                "filters": filters,
                "conversation_id": conversation_id,
                "hit_count": len(hits)
            },
            "usage": {}
        }), 200
    except Exception as e:
        return jsonify({"error": "query_failed", "detail": str(e)}), 500

@app.route("/search_vector_db", methods = ["POST"])
def search_vector_db():
    return jsonify(message="PLACEHOLDER_SEARCH_VECTOR_DB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))