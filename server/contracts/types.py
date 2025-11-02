from typing import TypedDict, List, Dict, Any

class Chunk(TypedDict):
    doc_id: str
    page: int
    chunk_id: str
    title: str
    text: str

class Hit(TypedDict):
    doc_id: str
    page: int
    title: str
    text: str
    score: float
    cite_id: int
