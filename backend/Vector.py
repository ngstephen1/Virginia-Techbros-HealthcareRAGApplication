import requests


API_KEY = "key goes here (from IBM Cloud)"


def get_iam_token(api_key):

    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={api_key}"

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status() # Raises an error for bad responses
        token_data = response.json()
        print("Successfully generated IAM token.")
        return token_data.get("access_token")
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting IAM token: {e}")

        if response.text:
            print(f"Response body: {response.text}")
        return None