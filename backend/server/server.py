from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from pypdf import PdfReader

'''loads environment variables from .env file'''
load_dotenv()
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

    # TODO: later call orchestrator.ingest_document(file)
    # For now, return a stub so FE can proceed.
    return jsonify({
        "id": "stub-doc-id",
        "title": file.filename,
        "page_count": 0,        # will be real later
        "chunk_count": 0        # will be real later
    }), 201

@app.route("/ingest_user_query", methods = ["POST"])
def ingest_user_query():
    payload = request.get_json(force=True, silent=False)
    validate_query(payload)

    prompt = payload["prompt"]
    top_k = payload.get("top_k", 5)
    filters = payload.get("filters")
    conversation_id = payload.get("conversation_id")

    # TODO: later call orchestrator.answer_query(...)
    # For now, deterministic stub so UI can develop:
    return jsonify({
        "answer": f"(stubbed) You asked: {prompt}",
        "citations": [],
        "retrieval": {"top_k": top_k, "filters": filters, "conversation_id": conversation_id},
        "usage": {}
    }), 200

@app.route("/search_vector_db", methods = ["POST"])
def search_vector_db():
    return jsonify(message="PLACEHOLDER_SEARCH_VECTOR_DB")


if __name__ == "__main__":
    app.run(debug = True, port= 5050)