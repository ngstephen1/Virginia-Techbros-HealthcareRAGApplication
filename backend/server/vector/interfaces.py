from typing import Protocol, List, Dict, Any, TypedDict

class Chunk(TypedDict):
    doc_id: str
    page: int
    chunk_id: str
    text: str
    title: str

class VectorStore(Protocol):
    def upsert(self, chunks: List[Chunk]) -> None: ...
    def search(self, query_vec: List[float], top_k: int = 20) -> List[Dict[str, Any]]: ...

class Embedder(Protocol):
    def embed_texts(self, texts: List[str]) -> List[List[float]]: ...