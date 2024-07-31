import requests
import pandas as pd
import os


# Base URL for the Census API
base_url = "https://api.open.fec.gov/v1/"

# Parameters for the API request
params = {
    "committee": "C00271007",
    "year": 2024,
    "page":
    "api_key": os.environ["FEC_API_KEY"]
}


# Make the API request
response = requests.get(base_url, params = params)
response.status_code

# Check if the request was successful
if response.status_code == 200:
    try:
        data = response.json()
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Raw response: {response.text}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response text: {response.text}")