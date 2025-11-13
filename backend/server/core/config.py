import os
from dotenv import load_dotenv
from backend.server.vector.wx_adapter import WatsonEmbedder
from backend.server.vector.milvus_store import MilvusStore
load_dotenv()

class Cfg:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    PORT = os.getenv("PORT", "8000") # Changed to 8000 to match your Docker command
    INDEX_PATH = os.getenv("INDEX_PATH", "./data/index")
    # This path is correct for save_only.py
    DOC_STORE  = os.getenv("DOC_STORE", "./data/medical_papers")
    # This EMBED_MODEL is for the mock store. Your real adapter overrides this.
    EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

cfg = Cfg()


print("Initializing application-wide WatsonEmbedder...")
# This will load keys from .env and get the IBM token
_embedder_instance = WatsonEmbedder()

print("Initializing application-wide MilvusStore...")
# This connects to your medical_rag.db file
_store_instance = MilvusStore(embedder=_embedder_instance)


## Fucntions to get the shared instances, hybrid.py will call these functions to get the real instances
def get_embedder():
    """Returns the shared instance of the WatsonEmbedder."""
    return _embedder_instance
def get_store():
    """Returns the shared instance of the MilvusStore."""
    return _store_instance