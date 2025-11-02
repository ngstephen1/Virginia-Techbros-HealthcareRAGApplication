import os
from dotenv import load_dotenv
load_dotenv()

class Cfg:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    PORT = os.getenv("PORT", "5001")
    INDEX_PATH = os.getenv("INDEX_PATH", "./data/index")
    DOC_STORE  = os.getenv("DOC_STORE", "./data/pdfs")
    EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

cfg = Cfg()