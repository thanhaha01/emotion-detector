import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze"
    api_key = "YOUR_API_KEY"

    headers = {"Content-Type": "application/json"}
    params = {"version": "2021-08-01"}
    data = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }

    response = requests.post(url, headers=headers, params=params, auth=("apikey", api_key), json=data)

    if response.status_code == 200:
        emotions = response.json()['emotion']['document']['emotion']
        dominant = max(emotions, key=emotions.get)
        return {"emotion": dominant, "emotion_scores": emotions}
    else:
        return {"error": f"API failed with status {response.status_code}"}
Add emotion detection logic
