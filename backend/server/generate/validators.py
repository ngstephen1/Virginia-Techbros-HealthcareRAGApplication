import re
def used_ids(answer: str) -> set[int]:
    return set(int(x) for x in re.findall(r'\[(\d+)\]', answer))
def scrub_orphans(answer: str, max_id: int) -> str:
    def repl(m):
        n=int(m.group(1));  return f"[{n}]" if 1<=n<=max_id else ""
    return re.sub(r'\[(\d+)\]', repl, answer)
def has_any_citation(answer: str) -> bool:
    return bool(re.search(r'\[\d+\]', answer))
