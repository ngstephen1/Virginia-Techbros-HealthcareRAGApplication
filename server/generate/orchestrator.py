from typing import List, Dict, Any
from server.generate.validators import scrub_orphans, has_any_citation
from server.generate.granite_adapter import call_granite
'''add inititializer'''
def build_prompt(question: str, snippets: List[Dict[str,Any]]) -> str:
    ctx="\n".join([f"[{i+1}] {s['title']} (p.{s.get('page',1)}): {s['text'][:800]}" for i,s in enumerate(snippets)])
    return (f"You are a medical research assistant. Answer ONLY from the snippets and cite them as [n]. "
            f"If insufficient, say so.\nQuestion: {question}\n\nSnippets:\n{ctx}\n\nAnswer:")

def synthesize(question: str, snippets: List[Dict[str,Any]]) -> str:
    # Try Granite first (no-op until wired)
    prompt_str = build_prompt(question, snippets)
    ans = call_granite(prompt_str)
    if not ans:
        # Deterministic fallback for local dev
        lines=[]
        for i,s in enumerate(snippets[:3],1):
            lines.append(f"- {s['text'][:220].rsplit('.',1)[0]}. [{i}]")
        ans = "Key findings:\n" + "\n".join(lines)
    # Enforce “no source, no claim”
    ans = scrub_orphans(ans, max_id=len(snippets))
    if not has_any_citation(ans):
        ans = "Insufficient grounded evidence in provided snippets."
    return ans
