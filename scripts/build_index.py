import json, glob
from pathlib import Path
from typing import List, Dict, Any
from server.embeddings.wx_adapter import Embedder

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
