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
        print("IAM: no API key found", flush=True)
        return None
    try:
        r = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": API_KEY,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=30,
        )
        print("IAM token status:", r.status_code, flush=True)
        if r.status_code != 200:
            print("IAM response text:", r.text[:300], flush=True)
            return None
        data = r.json()
        return data.get("access_token")
    except Exception as e:
        print("IAM exception:", e, flush=True)
        return None
    

'''HTTP call to watsonx.ai granite returns generated test or none'''
def call_granite(
    prompt_str: str,
    snippets: Optional[List[Dict[str, Any]]] = None,
) -> Optional[str]:
    """
    Call watsonx.ai Granite with a fully formatted prompt string.
    `snippets` is ignored for now but kept for future use.
    """
    token = iam_token()
    if not token:
        return "IBM IAM token could not be obtained. Check WX_API_KEY."
    
    if not PROJECT_ID or not MODEL_ID:
        return "WX_PROJECT_ID or WX_MODEL_ID missing. Check your environment variables."
    
    try:
        url = f"{REGION_URL}/ml/v1/text/generation"

        #  Only 'version' in query params
        params = {"version": "2023-05-29"}

        payload = {
            "model_id": MODEL_ID,
            "input": prompt_str,
            # tell watsonx which project to bill/use
            "project_id": PROJECT_ID,
            # "projectId": PROJECT_ID,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 512,
                "repetition_penalty": 1.05,
    },
        }

        #  Put project_id in the header instead
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        res = requests.post(
            url, params=params, json=payload, headers=headers, timeout=60
        )

        if res.status_code in (401, 403):
            return (
                f"Unauthorized ({res.status_code}). "
                f"Check WX_API_KEY, WX_PROJECT_ID, WX_REGION: {res.text[:200]}"
            )

        if res.status_code != 200:
            return f"Granite HTTP {res.status_code}: {res.text[:200]}"

        data = res.json()
        results = data.get("results") or []
        if not results:
            return "Granite call succeeded but returned no results."
        return results[0].get("generated_text")
    except Exception as e:
        return f"Exception while calling Granite: {e}"