import glob
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from backend.server.vector.wx_adapter import WatsonEmbedder
from backend.server.vector.milvus_store import MilvusStore, MILVUS_DB_PATH

MEMORY_INDEX_PATH = Path("backend/data/index/memory_index.json")


def load_chunks() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for fp in glob.glob("chunks/*.jsonl"):
        with open(fp, "r") as fh:
            for line in fh:
                row = json.loads(line)
                rows.append(
                    {
                        "doc_id": row["doc_id"],
                        "page": int(row["page"]),
                        "chunk_id": row["chunk_id"],
                        "title": row.get("title", ""),
                        "text": row["text"],
                    }
                )
    print(f"Found {len(rows)} chunks to process from 'chunks/' folder.")
    return rows


def write_memory_index(chunks: List[Dict[str, Any]], vecs: List[List[float]]) -> None:
    items = []
    for chunk, vec in zip(chunks, vecs):
        entry = dict(chunk)
        entry["vec"] = vec
        items.append(entry)
    MEMORY_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_INDEX_PATH.write_text(json.dumps({"items": items}))
    print(f"Wrote {len(items)} vectors → {MEMORY_INDEX_PATH}")


def upsert_milvus(chunks: List[Dict[str, Any]], vecs: List[List[float]], embedder: WatsonEmbedder) -> None:
    try:
        store = MilvusStore(embedder=embedder)
    except Exception as exc:
        print(f"Milvus unavailable ({exc}); skipping vector DB upsert.")
        return

    if store.client is None:
        print("Milvus client not available; skipping vector DB upsert.")
        return

    records = []
    for chunk, vec in zip(chunks, vecs):
        payload = dict(chunk)
        payload["vector"] = vec
        records.append(payload)

    print(f"Inserting {len(records)} vectors into Milvus at {MILVUS_DB_PATH}...")
    store.upsert(records)
    print("Milvus upsert complete.")


def main() -> None:
    chunks = load_chunks()
    if not chunks:
        print("No chunks found in chunks/*.jsonl. Run run_chunker.py first.")
        return

    print("Initializing WatsonEmbedder...")
    embedder = WatsonEmbedder()

    texts = [c["text"] for c in chunks]
    print(f"Embedding {len(texts)} text chunks...")
    vectors = embedder.embed_texts(texts)
    print("Embedding complete.")

    write_memory_index(chunks, vectors)
    upsert_milvus(chunks, vectors, embedder)


if __name__ == "__main__":
    Path(MILVUS_DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    main()
