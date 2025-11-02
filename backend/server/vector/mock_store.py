# Dev-only, to be replaced by Raf's Milvus/watsonx.data implementation
from typing import List, Dict, Any
from pathlib import Path
from server.core.config import cfg

# simple in-memory collection
_STORE: List[Dict[str, Any]] = []

def preload_demo_chunks():
    """Optional: create a few fake chunks if index is empty."""
    global _STORE
    if _STORE: return
    _STORE = [
        {"doc_id":"demo1","page":1,"chunk_id":"demo1-1","title":"Hypertension Study",
         "text":"In adults with stage 1 hypertension, lifestyle modification reduces systolic BP by 5 to 7 mmHg."},
        {"doc_id":"demo2","page":3,"chunk_id":"demo2-3","title":"Diabetes Meta-analysis",
         "text":"Metformin is first-line therapy for type 2 diabetes unless contraindicated according to ADA guidelines."},
        {"doc_id":"demo3","page":2,"chunk_id":"demo3-2","title":"RSV Vaccine Trial",
         "text":"The vaccine reduced RSV-related hospitalizations with a relative risk of 0.72 compared to placebo."},
    ]

class SimpleEmbedder:
    def __init__(self):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(cfg.EMBED_MODEL)
        except Exception:
            self.model = None

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        if self.model:
            return self.model.encode(texts, normalize_embeddings=True).tolist()
        # hash fallback (very weak, dev-only)
        import math
        vecs=[]
        for t in texts:
            s = sum(ord(c) for c in t) or 1
            vecs.append([math.sin(s%1000), math.cos(s%1000)])
        return vecs

def _cos(a,b):
    import math
    num=sum(x*y for x,y in zip(a,b))
    da=math.sqrt(sum(x*x for x in a)); db=math.sqrt(sum(x*x for x in b))
    return num/(da*db+1e-9)

class MockStore:
    def __init__(self, embedder: SimpleEmbedder):
        self.emb = embedder
        preload_demo_chunks()
        if _STORE and "vec" not in _STORE[0]:
            for it in _STORE:
                it["vec"] = self.emb.embed_texts([it["text"]])[0]

    def upsert(self, chunks: List[Dict[str,Any]]) -> None:
        for ch in chunks:
            ch = dict(ch)
            ch["vec"] = self.emb.embed_texts([ch["text"]])[0]
            _STORE.append(ch)

    def search(self, query_vec: List[float], top_k: int = 20) -> List[Dict[str, Any]]:
        scored = [(it, _cos(query_vec, it["vec"])) for it in _STORE]
        scored.sort(key=lambda x: x[1], reverse=True)
        out=[]
        for it, score in scored[:top_k]:
            d = {k:it[k] for k in ["doc_id","page","title","text"]}
            d["score"]=float(score)
            out.append(d)
        return out

# factories for the API app
def get_embedder(): return SimpleEmbedder()
def get_store(): return MockStore(get_embedder())