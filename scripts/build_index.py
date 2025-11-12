import json, glob
from pathlib import Path
from typing import List, Dict, Any
from server.embeddings.wx_adapter import Embedder
from pymilvus import MilvusClient, DataType

# --- Milvus Configuration ---
MILVUS_DB_PATH = "data/index/medical_rag.db"
COLLECTION_NAME = "medical_papers"
VECTOR_DIMENSION = 768
import json
import glob
from pathlib import Path
from typing import List, Dict, Any

# Import your NEW, REAL classes
from backend.server.vector.wx_adapter import WatsonEmbedder
from backend.server.vector.milvus_store import MilvusStore, MILVUS_DB_PATH

def load_chunks() -> List[Dict[str, Any]]:
    """Loads text chunks from the 'chunks' directory."""
    rows = []
    # Make sure your current working directory is the project root
    for fp in glob.glob("chunks/*.jsonl"):
        with open(fp, "r") as f:
            for line in f:
                row = json.loads(line)
                rows.append({
                    "doc_id": row["doc_id"],
                    "page": int(row["page"]),
                    "chunk_id": row["chunk_id"],
                    "title": row.get("title", ""),
                    "text": row["text"],
                })
    print(f"Found {len(rows)} chunks to process from 'chunks/' folder.")
    return rows

def main():
    # 1. Load the text chunks from .jsonl files
    chunks = load_chunks()
    if not chunks:
        print("No chunks found in chunks/*.jsonl. Run the ingest script first.")
        return

    # 2. Initialize the REAL embedder (This gets the IBM token)
    print("Initializing IBM WatsonEmbedder...")
    emb = WatsonEmbedder()

    # 3. Vectorize all text chunks in a batch
    print(f"Embedding {len(chunks)} text chunks with IBM watsonx.ai... (this may take a moment)")
    texts_to_embed = [c["text"] for c in chunks]
    vecs = emb.embed_texts(texts_to_embed)
    print("Text embedding complete.")

    # 4. Combine chunks with their new vectors
    data_to_insert = []
    for c, v in zip(chunks, vecs):
        c["vector"] = v  # Add the 'vector' key
        data_to_insert.append(c)

    # 5. Initialize the REAL vector store
    # This will create/connect to 'data/index/medical_rag.db'
    print(f"Initializing MilvusStore at {MILVUS_DB_PATH}...")
    # We pass the embedder so the store knows the vector dimension
    store = MilvusStore(embedder=emb) 
    
    # 6. Insert the vectorized data into Milvus
    print(f"Inserting {len(data_to_insert)} vectors into Milvus...")
    store.upsert(data_to_insert)
    
    print(f"--- Successfully wrote {len(data_to_insert)} vectors to Milvus! ---")

if __name__ == "__main__":
    # Ensure the 'data/index' directory exists
    Path(MILVUS_DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    main()
OUT = Path("data/index/memory_index.json")

def load_chunks() -> List[Dict[str,Any]]:
    rows=[]
    for fp in glob.glob("chunks/*.jsonl"):
        with open(fp, "r") as f:
            for line in f:
                row = json.loads(line)
                rows.append({
                    "doc_id": row["doc_id"],
                    "page": int(row["page"]),
                    "chunk_id": row["chunk_id"],
                    "title": row.get("title",""),
                    "text": row["text"],
                })
    return rows

def main():
    chunks = load_chunks()
    if not chunks:
        print("No chunks found in chunks/*.jsonl"); return
    emb = Embedder()
    vecs = emb.embed_texts([c["text"] for c in chunks])
    items=[]
    for c,v in zip(chunks, vecs):
        it=dict(c); it["vec"]=v; items.append(it)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"items": items}))
    print(f"Wrote {len(items)} vectors → {OUT}")
if __name__ == "__main__":
    main()
