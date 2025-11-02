from flask import Flask, request, jsonify
from server.core.config import cfg
from server.retrieval.hybrid import hybrid_retrieve
from server.generate.answer import synthesize_with_citations
from server.vector.mock_store import get_store, get_embedder  # dev-only mock
from server.ingest.save_only import save_pdfs                 # no chunking: Raf owns it

app = Flask(__name__)

@app.get("/health")
def health(): return {"ok": True, "env": cfg.FLASK_ENV}

@app.post("/ingest")
def ingest():
    """MVP: save PDFs only (no parsing here). Raf will replace with real chunk/index step."""
    files = request.files.getlist("files")
    doc_ids = save_pdfs(files)
    return jsonify({"doc_ids": doc_ids})

@app.post("/query")
def query():
    data = request.get_json(force=True)
    question = data["question"].strip()
    k = int(data.get("k", 8))
    # Dev path: use mock embedder/store. Raf will inject Milvus/watsonx.data later.
    store = get_store()
    embedder = get_embedder()
    hits = hybrid_retrieve(question, embedder, store, k=k)
    result = synthesize_with_citations(question, hits)
    return jsonify(result)

@app.get("/doc/<doc_id>/page/<int:p>")
def page_text(doc_id, p):
    """Dev path: we don't parse pages yet; return stub text to unblock FE."""
    return jsonify({"doc_id": doc_id, "page": p, "text": "Page preview coming from Raf's parser."})

def create_app(): return app

if __name__ == "__main__":
    app.run(debug=True, port=int(cfg.PORT))