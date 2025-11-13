from pymilvus import MilvusClient, DataType
from typing import List, Dict, Any
from .wx_adapter import WatsonEmbedder


# --- Milvus Configuration ---
MILVUS_DB_PATH = "backend/data/index/medical_rag.db"
COLLECTION_NAME = "medical_papers"

class MilvusStore:
    
    def __init__(self, embedder: WatsonEmbedder):
        print(f"Initializing MilvusStore. Connecting to: {MILVUS_DB_PATH}")
        self.dimension = embedder.dimension
        self.client = MilvusClient(uri=MILVUS_DB_PATH)
        
        if not self.client.has_collection(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' not found. Creating it.")
            self._create_collection()
        else:
            print(f"Connected to Milvus collection: '{COLLECTION_NAME}'")

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
        if not chunks:
            return
        
        print(f"Upserting {len(chunks)} chunks into Milvus...")
        res = self.client.insert(collection_name=COLLECTION_NAME, data=chunks)
        print(f"Successfully inserted {res['insert_count']} chunks.")

    def search(self, query_vec: List[float], top_k: int = 20) -> List[Dict[str, Any]]:
        """
        Searches the Milvus database for the most similar vectors.
        """
        search_res = self.client.search(
            collection_name=COLLECTION_NAME,
            data=[query_vec],  # Milvus expects a list of vectors
            limit=top_k,
            output_fields=["doc_id", "page", "title", "text", "chunk_id"]
        )
        
        hits:  List[Dict[str, Any]] = []
        for result in search_res[0]: # Results for the first (only) query vector
            hit_data = result['entity']
            hit_data["score"] = result['distance'] # 'distance' is the score
            hits.append(hit_data)
            
        return hits