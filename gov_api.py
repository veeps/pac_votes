import requests
import pandas as pd
import os


# Base URL for the Census API
base_url = "https://api.congress.gov/v3/bill/"
base_url
# Parameters for the API request
params = {
    "congress": "118",
    "billType": "hr",
    "billNumber": "2365",
    "api_key": os.environ["GOV_API_KEY"]
}

# Make the API request
response = requests.get(base_url, params = params)
response.status_code
data = response.json()

data["bills"]

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

data.keys