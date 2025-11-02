from typing import List
import math

class Embedder:
    """
    IBM watsonx.ai embeddings can be wired later.
    For now, a tiny pure-Python fallback so nothing compiles.
    """
    def __init__(self) -> None:
        pass

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        vecs=[]
        for t in texts:
            s = sum(ord(c) for c in t) or 1
            vecs.append([math.sin(s % 997), math.cos(s % 991)])
        return vecs
