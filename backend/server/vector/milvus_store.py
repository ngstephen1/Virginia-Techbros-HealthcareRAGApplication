from pymilvus import MilvusClient, DataType
import numpy as np
import json
import math
from pathlib import Path
from typing import List, Dict, Any
from .wx_adapter import WatsonEmbedder


# --- Milvus Configuration ---
# medical_rag needs to match the embedding dimension
MILVUS_DB_PATH = "backend/data/index/medical_rag.db"
MEMORY_INDEX_PATH = Path("backend/data/index/memory_index.json")
COLLECTION_NAME = "medical_papers"

class MilvusStore:
    
    def __init__(self, embedder: WatsonEmbedder):
        print(f"Initializing MilvusStore. Connecting to: {MILVUS_DB_PATH}")
        self.dimension = embedder.dimension
        self.client = None
        self._memory_items = None
        try:
            self.client = MilvusClient(uri=MILVUS_DB_PATH)
            
            if not self.client.has_collection(COLLECTION_NAME):
                print(f"Collection '{COLLECTION_NAME}' not found. Creating it.")
                self._create_collection()
            else:
                print(f"Connected to Milvus collection: '{COLLECTION_NAME}'")
        except Exception as exc:
            print(f"Milvus connection failed ({exc}). Falling back to memory index.")
            if MEMORY_INDEX_PATH.exists():
                data = json.loads(MEMORY_INDEX_PATH.read_text())
                self._memory_items = data.get("items", [])
            else:
                print("Memory index file not found; retrieval will return empty results.")

    def _create_collection(self):
        schema = MilvusClient.create_schema(auto_id=True, enable_dynamic_field=False)
        schema.add_field("id", DataType.INT64, is_primary=True)
        schema.add_field("vector", DataType.FLOAT_VECTOR, dim=self.dimension)
        schema.add_field("doc_id", DataType.VARCHAR, max_length=1000)
        schema.add_field("page", DataType.INT64)
        schema.add_field("chunk_id", DataType.VARCHAR, max_length=1000)
        schema.add_field("title", DataType.VARCHAR, max_length=1000)
        schema.add_field("text", DataType.VARCHAR, max_length=65535)

        self.client.create_collection(collection_name=COLLECTION_NAME,schema=schema)
        
        index_params = self.client.prepare_index_params(
            field_name="vector", metric_type="COSINE", index_type="AUTOINDEX"
        )
        self.client.create_index(COLLECTION_NAME, index_params)
        print("Created new Milvus collection and index.")

    def upsert(self, chunks: List[Dict[str, Any]]) -> None:
        """
        Inserts chunks into Milvus.
        NOTE: This expects the 'vector' key to already be in the chunks.
        """
        if not chunks or self.client is None:
            return
        
        print(f"Upserting {len(chunks)} chunks into Milvus...")
        res = self.client.insert(collection_name=COLLECTION_NAME, data=chunks)
        print(f"Successfully inserted {res['insert_count']} chunks.")

    def _to_float32(self, vec: List[float]):
        return np.asarray(vec, dtype="float32").tolist()

    def _cosine(self, a: List[float], b: List[float]) -> float:
        dot = sum(x*y for x, y in zip(a, b))
        na = math.sqrt(sum(x*x for x in a))
        nb = math.sqrt(sum(x*x for x in b))
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    def search(self, query_vec: List[float], top_k: int = 20) -> List[Dict[str, Any]]:
        """
        Searches the Milvus database for the most similar vectors.
        """
        dense_vec = self._to_float32(query_vec)
        if dense_vec:
            print(f"[MilvusStore] Query vector dtype sample: {type(dense_vec[0])}, len={len(dense_vec)}")

        if self.client is None:
            if not self._memory_items:
                return []
            scored=[]
            for item in self._memory_items:
                vec = item.get("vec") or []
                score = self._cosine(dense_vec, vec)
                scored.append((item, score))
            scored.sort(key=lambda x: x[1], reverse=True)
            hits=[]
            for it, score in scored[:top_k]:
                hits.append({
                    "doc_id": it["doc_id"],
                    "page": it["page"],
                    "title": it.get("title",""),
                    "text": it["text"],
                    "score": float(score),
                    "chunk_id": it.get("chunk_id","")
                })
            return hits

        search_res = self.client.search(
            collection_name=COLLECTION_NAME,
            data=[dense_vec],  # Milvus expects a list of vectors
            anns_field="vector",
            search_params={"metric_type": "COSINE"},
            limit=top_k,
            output_fields=["doc_id", "page", "title", "text", "chunk_id"]
        )
        
        hits:  List[Dict[str, Any]] = []
        for result in search_res[0]: # Results for the first (only) query vector
            hit_data = result['entity']
            hit_data["score"] = result['distance'] # 'distance' is the score
            hits.append(hit_data)
            
        return hits
