from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from backend.server.ingest import save_only
from backend.server.generate import answer 
from backend.server.retrieval import hybrid
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
    except Exception as e:
        raise ValueError("PDF could not be parsed") from e
    
def validate_query(user_query):
    #validate the JSON body for RAG queries

    if not isinstance(user_query, dict):
        raise ValueError("Invalid JSON body")
    prompt = str(user_query.get("prompt", "")).strip()
    if not prompt:
        raise ValueError ("Field prompt is required")
    top_k = user_query.get("top_k", 5)

@app.post("/dev/summarize_hits")
def dev_summarize_hits():
    body = request.get_json(force=True, silent=False)

    question = str(body.get("prompt", "")).strip()
    hits = body.get("hits", [])
    if not question or not isinstance(hits, list):
        return jsonify({"error": "Provide prompt and hits[]"}), 400

    # make sure cite_id exists for your _citations() logic
    for i, h in enumerate(hits, start=1):
        h.setdefault("cite_id", i)

    result = answer.synthesize_with_citations(question, hits)
    return jsonify(result), 200

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
    validate_upload_pdf(file)
    try:
        result = save_only.ingest(file.stream, filename= file.filename)
        resp = {
            "id": result.get("doc_id") or result.get("id") or "unknown",
            "title": result.get("title", file.filename),
            "page_count": int(result.get("page_couunt",0)),
            "chunk_count": int(result.get("chunk_count",0)),
        }
        return jsonify(resp), 201
    except Exception as e:
        return jsonify({"error": "ingestion failed", "detail":str(e)}), 500

    # TODO: later call orchestrator.ingest_document(file)
    # For now, return a stub so FE can proceed.

@app.post("/ingest_user_query")
def ingest_user_query():
    payload = request.get_json(force=True, silent=False)
    validate_query(payload)

    question = payload["prompt"]
    top_k = payload.get("top_k", 5)
    filters = payload.get("filters")
    conversation_id = payload.get("conversation_id")
    hits = hybrid.retrieve (question, top_k=top_k, filters=filters)
    for i, h in enumerate(hits, start=1):
        h.setdefault("cite_id", i)
    
    result = answer._answer_from_snippets(question, hits)
    # TODO: later call orchestrator.answer_query(...)
    # For now, deterministic stub so UI can develop:
    return jsonify({
        "answer": result.get("anser", ""),
        "citations": result.get("citations",[]),
        "retrieval": {"top_k": top_k, "filters": filters, "conversation_id":payload.get("conversation_id")},
        "usage": {}
    }), 200

@app.route("/search_vector_db", methods = ["POST"])
def search_vector_db():
    return jsonify(message="PLACEHOLDER_SEARCH_VECTOR_DB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))