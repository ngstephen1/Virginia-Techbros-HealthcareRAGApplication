import os
import pypdf
import json
from pathlib import Path
from typing import List


# --- CONFIGURATION ---
PDF_SOURCE_DIR = Path("data/medical_papers")
CHUNK_OUTPUT_DIR = Path("chunks")
CHUNK_SIZE = 500  # Number of words per chunk
OVERLAP = 50      # Number of words to overlap between chunks


def chunk_text(doc_id: str, title: str, full_text: str) -> List[dict]:
    """Splits a single document's text into overlapping chunks."""
    words = full_text.split()
    chunks = []
    chunk_num = 0
    
    for i in range(0, len(words), CHUNK_SIZE - OVERLAP):
        chunk_text = " ".join(words[i:i + CHUNK_SIZE])
        
        # This is the exact format 'build_index.py' expects
        chunks.append({
            "doc_id": doc_id,
            "page": 0, # Note: pypdf splitting by page is complex, 0 is a placeholder
            "chunk_id": f"{doc_id}:{chunk_num:03d}",
            "title": title,
            "text": chunk_text,
        })
        chunk_num += 1
    return chunks

def main():
    print(f"Checking for PDFs in: {PDF_SOURCE_DIR}")
    pdf_files = list(PDF_SOURCE_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print(f"Error: No PDF files found in '{PDF_SOURCE_DIR}'.")
        print(f"Please add your PDFs (like Advancement_AI.pdf) to that folder.")
        return

    # Ensure the 'chunks' directory exists
    CHUNK_OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Found {len(pdf_files)} PDFs to chunk...")

    for pdf_path in pdf_files:
        try:
            doc_id = pdf_path.stem  # e.g., "Advancement_AI"
            print(f"  -> Processing: {pdf_path.name} (doc_id: {doc_id})")
            
            with open(pdf_path, 'rb') as f:
                reader = pypdf.PdfReader(f)
                full_text = ""
                for page in reader.pages:
                    full_text += page.extract_text() + "\n"
            
            # Digest the text into chunks
            chunks = chunk_text(doc_id, title=doc_id.replace("_", " "), full_text=full_text)
            
            # Write to a new .jsonl file
            output_file = CHUNK_OUTPUT_DIR / f"{doc_id}.jsonl"
            with open(output_file, 'w') as f:
                for chunk in chunks:
                    f.write(json.dumps(chunk) + "\n")
            
            print(f"     Successfully created {len(chunks)} chunks in {output_file}")
            
        except Exception as e:
            print(f"     Failed to process {pdf_path.name}: {e}")

    print("\nChunking complete.")

if __name__ == "__main__":
    main()