"""
watsonx Discovery retriever (IBM-only).
TODO (with creds): call Discovery search and map to List[Hit] from server/contracts/types.
Env: IBM_API_KEY, IBM_REGION, WXD_PROJECT_ID, WXD_COLLECTION_ID
"""
from typing import List
from server/contracts/types import Hit

def discovery_search(question: str, k: int = 8) -> List[Hit]:
    # Placeholder so FE/BE can integrate now
    demo = [
        {"doc_id":"demoA","page":1,"title":"Hypertension Study",
         "text":"Lifestyle modification reduces systolic BP by ~5–7 mmHg.", "score":0.92, "cite_id":1},
        {"doc_id":"demoB","page":3,"title":"Diabetes Meta-analysis",
         "text":"Metformin is first-line therapy for type 2 diabetes.", "score":0.88, "cite_id":2},
    ]
    return demo[:k]
