import uuid
from pathlib import Path
from typing import List
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from backend.server.core.config import cfg

def save_pdfs(files: List[FileStorage]):
    target = Path(cfg.DOC_STORE)
    target.mkdir(parents=True, exist_ok=True)

    ids=[]
    for f in files:
        if not isinstance(f, FileStorage):
            raise TypeError(f"Expected FileStorage, got {type(f).__name__}")
        doc_id = uuid.uuid4().hex[:8]
        _client_name = secure_filename(f.filename or "upload.pdf")
        out = target / f"{doc_id}.pdf"
        f.save(str(out))
        ids.append(doc_id)
    return ids