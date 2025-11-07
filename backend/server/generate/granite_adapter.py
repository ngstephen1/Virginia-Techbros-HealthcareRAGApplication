"""
watsonx.ai Granite generator (IBM-only).
TODO (with creds): call Granite with numbered snippets, low temp, return answer text with [n].
Env: IBM_API_KEY, IBM_REGION, GRANITE_MODEL_ID
"""
from typing import List, Dict, Any, Optional
import os, time, requests

API_KEY   = os.getenv("WX_API_KEY")
PROJECT_ID = os.getenv("WX_PROJECT_ID")
MODEL_ID  = os.getenv("WX_MODEL_ID", "granite-3-8b-instruct")
REGION_URL = os.getenv("WX_REGION_URL") or f"https://{os.getenv('WX_REGION','us-south')}.ml.cloud.ibm.com"
'''Uses .env variables'''
def iam_token() -> Optional[str]:
    if not API_KEY:
        return None
    try:
        r = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            data ={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": API_KEY,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=30, 
        )
        if r.status_code != 200:
            return None
        return r.json.get("access_token")
    except Exception:
        return None
'''HTTP call to watsonx.ai granite returns generated test or none'''
def call_granite(question: str, snippets: List[Dict[str, Any]]) -> str | None:
    token = iam_token()
    if not token:
        return "Provide a valid token"
    if not PROJECT_ID or not MODEL_ID:
        return "Provide a valid token"
    
    try:
        url = f"{REGION_URL}/ml/v1/text/generation"
        params = {"version": "2023-05-29", "project_id": PROJECT_ID}
        payload = {
            "model_id": MODEL_ID,
            "input": prompt_str,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 512,
                "repetition_penalty": 1.05
            }

        }
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        res = requests.post(url, params=params, json=payload, headers = headers, timeout = 60)
        if res.status_code in (401,403):
            return "provide a valid token"
        if res.status_code != 200:
            return None
        date = res.json()
        return (data.get("results") or [{}])[0].get("generated_text")
    except Exception:
        return None  # returns None until IBM creds are set; orchestration falls back deterministically
