from typing import List, Dict, Any
from rank_bm25 import BM25Okapi

def hybrid_retrieve(question: str, embedder, store, k: int = 8) -> List[Dict[str, Any]]:
    """
    1) Vector search (k*3 candidates)
    2) BM25 rerank over those candidates
    """
    qv = embedder.embed_texts([question])[0]
    v_hits = store.search(qv, top_k=max(10, k*3))  # [{text, doc_id, page, score}]
    if not v_hits:
        return []

    corpus = [h["text"] for h in v_hits]
    bm25 = BM25Okapi([c.split() for c in corpus])
    scores = bm25.get_scores(question.split())
    ranked = sorted(zip(v_hits, scores), key=lambda x: x[1], reverse=True)
    hits = [h for h,_ in ranked[:k]]

    # assign stable cite_ids used in answer text
    for i, h in enumerate(hits, start=1): h["cite_id"] = i
    return hits