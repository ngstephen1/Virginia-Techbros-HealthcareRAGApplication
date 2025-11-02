import uuid
from pathlib import Path
from typing import List
from werkzeug.datastructures import FileStorage
from server.core.config import cfg

def save_pdfs(files: List[FileStorage]):
    Path(cfg.DOC_STORE).mkdir(parents=True, exist_ok=True)
    ids=[]
    for f in files:
        doc_id = uuid.uuid4().hex[:8]
        out = Path(cfg.DOC_STORE, f"{doc_id}.pdf")
        f.save(out)
        ids.append(doc_id)
    return ids