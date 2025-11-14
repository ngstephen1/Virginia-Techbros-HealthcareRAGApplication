import os
import math
import requests
from typing import List
from dotenv import load_dotenv
from pathlib import Path

# Load .env variables from backend/server/.env
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path) 

class WatsonEmbedder:
    """
    This class implements the 'Embedder' protocol using the IBM watsonx.ai API.
    """
    
    def __init__(self):
        self.api_key = os.getenv("WX_API_KEY")
        self.watsonx_url = os.getenv("WX_REGION_URL")
        self.project_id = os.getenv("WX_PROJECT_ID")
        
        # This is the correct, high-performance model for embeddings
        self.model = "ibm/slate-125m-english-rtrvr"
        self.dimension = 768 # Vector dimension for the 'slate' model
        
        if not all([self.api_key, self.watsonx_url, self.project_id]):
            raise ValueError("Missing watsonx.ai credentials in .env file")
        
        self.iam_token = self._get_iam_token()
        self._mock_mode = False
        if not self.iam_token:
            print("WatsonEmbedder could not obtain IAM token. Falling back to mock embeddings.")
            self._mock_mode = True
        else:
            print("WatsonEmbedder initialized and token generated.")

    def _get_iam_token(self):
        """Exchanges the API Key for a temporary IAM access token."""
        url = "https://iam.cloud.ibm.com/identity/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={self.api_key}"
        
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status() 
            return response.json().get("access_token")
        except Exception as e:
            print(f"Error getting IAM token: {e}")
            return None

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        This is the required method from the 'Embedder' protocol.
        """
        if self._mock_mode:
            # deterministic fallback using hash of text
            vecs=[]
            for t in texts:
                s = sum(ord(c) for c in t) or 1
                vec = [math.sin((s+i) % 997) for i in range(self.dimension)]
                vecs.append(vec)
            return vecs

        if not self.iam_token:
            raise Exception("No valid IAM token.")

        api_url = f"{self.watsonx_url}/ml/v1/text/embeddings?version=2024-05-17"
        headers = {
            "Authorization": f"Bearer {self.iam_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "model_id": self.model,
            "input": texts, # Send batch of texts
            "project_id": self.project_id
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return [res["embedding"] for res in result["results"]]
        except requests.exceptions.RequestException as e:
            # Handle token expiration
            if getattr(e.response, "status_code", None) == 401:
                print("Token expired, refreshing...")
                self.iam_token = self._get_iam_token()
                return self.embed_texts(texts) # Retry once
            print(f"Error calling embedding API: {e}")
            if hasattr(e.response, 'text'): print(f"Response body: {e.response.text}")
            self._mock_mode = True
            return self.embed_texts(texts)
        except Exception as e:
            print(f"Embedding call failed ({e}). Using mock vectors.")
            self._mock_mode = True
            return self.embed_texts(texts)
