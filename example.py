#!python3
import requests
import json

# REPLACE WITH API LINK
api_url = "https://unsplattered-haematoid-trinity.ngrok-free.dev/"

# The payload: list of vehicles
payload = [
    {"length": 10, "quantity": 1}
]

# Make the POST request with JSON
response = requests.post(api_url, json=payload)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print("Response from API:")
    print(json.dumps(data, indent=2))
    print(len(data))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)