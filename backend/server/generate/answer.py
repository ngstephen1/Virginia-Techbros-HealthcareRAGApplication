from typing import List, Dict, Any

def _answer_from_snippets(question: str, hits: List[Dict[str, Any]]) -> str:
    """Dev-only deterministic answer with numbered citations."""
    lines = []
    for i, h in enumerate(hits[:3], start=1):
        snippet = h["text"].strip().split(". ")
        piece = (". ".join(snippet[:2]) + ".")[:220]
        lines.append(f"- {piece} [{i}]")
    return "Key findings:\n" + "\n".join(lines)

def _citations(hits: List[Dict[str, Any]]):
    return [{"cite_id":h["cite_id"], "doc_id":h["doc_id"], "page":h.get("page", 1), "span":[0, min(160, len(h["text"]))]} for h in hits]

def synthesize_with_citations(question: str, hits: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Future: call IBM Granite via watsonx.ai with strict JSON instructions.
    Post-process: drop any claim without [n]. For dev we return a structured stub.
    """
    if not hits:
        return {"answer":"No relevant passages found.", "citations": [], "sources": []}
    answer = _answer_from_snippets(question, hits)
    cits = _citations(hits)
    sources = {}
    for h in hits:
        s = sources.setdefault(h["doc_id"], {"doc_id":h["doc_id"], "title":h.get("title",""), "pages":set()})
        s["pages"].add(h.get("page",1))
    sources_list = [{"doc_id":sid, "title":s["title"], "pages":sorted(list(s["pages"]))} for sid, s in sources.items()]
    return {"answer": answer, "citations": cits, "sources": sources_list}