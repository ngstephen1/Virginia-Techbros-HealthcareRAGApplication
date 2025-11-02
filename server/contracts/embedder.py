from typing import Protocol, List

class Embedder(Protocol):
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        ...
