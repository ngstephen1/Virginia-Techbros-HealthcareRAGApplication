import sys, json, math
from typing import List, Dict, Any
from server.embeddings.wx_adapter import Embedder

INDEX = "data/index/memory_index.json"

def cos(a: List[float], b: List[float]) -> float:
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(x*x for x in b))
    return dot/(na*nb + 1e-9)

def retrieve(question: str, k: int = 8) -> List[Dict[str,Any]]:
    data = json.load(open(INDEX))
    qv = Embedder().embed_texts([question])[0]
    scored = [(it, cos(qv, it["vec"])) for it in data["items"]]
    scored.sort(key=lambda x: x[1], reverse=True)
    hits=[]
    for i,(it,score) in enumerate(scored[:k],1):
        hits.append({"doc_id":it["doc_id"], "page":it["page"], "title":it["title"],
                     "text":it["text"], "score":float(score), "cite_id":i})
    return hits

def synthesize(question: str, hits: List[Dict[str,Any]]) -> str:
    if not hits: return "Insufficient grounded evidence in provided snippets."
    lines=[]
    for i,h in enumerate(hits[:3],1):
        lines.append(f"- {h['text'][:220].rsplit('.',1)[0]}. [{i}]")
    ans = "Key findings:\n" + "\n".join(lines)
    return ans

def to_response(ans: str, hits: List[Dict[str,Any]]) -> Dict[str,Any]:
    cits=[{"cite_id":h["cite_id"],"doc_id":h["doc_id"],"page":h["page"],"span":[0, min(160, len(h['text']))]} for h in hits]
    src={}
    for h in hits:
        src.setdefault(h["doc_id"], {"doc_id":h["doc_id"], "title":h["title"], "pages":set()})
        src[h["doc_id"]]["pages"].add(h["page"])
    sources=[{"doc_id":k,"title":v["title"],"pages":sorted(list(v["pages"]))} for k,v in src.items()]
    return {"answer": ans, "citations": cits, "sources": sources}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/offline_query.py 'your question' [k]"); sys.exit(1)
    q = sys.argv[1]; k=int(sys.argv[2]) if len(sys.argv)>2 else 8
    hits = retrieve(q, k)
    ans  = synthesize(q, hits)
    print(json.dumps(to_response(ans, hits), indent=2))
