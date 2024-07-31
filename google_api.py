import requests
from google_civic_information_api import elections
import os
from urllib.parse import quote
import pandas as pd


base_url = "https://www.googleapis.com/civicinfo/v2/elections"
params = {
        "key": os.environ["GOOGLE_API"]
}

response = requests.get(base_url, params = params)
response.status_code
pd.DataFrame(response.json()['elections'])

geo_url = "https://www.googleapis.com/civicinfo/v2/voterinfo?&address=1311%20pacific%20apt%20306%20st%2C%20Brooklyn%2C%20NY%2011216-4591%2C%20USA&key=AIzaSyA5s-BpdlfUeOrKFRQuAqQdb1ASpG8jKmc"
response = requests.get(geo_url)
response.status_code


voter_url = "https://www.googleapis.com/civicinfo/v2/voterinfo"
address = "1311 pacific apt 306 st, Brooklyn, NY 11216-4591"
encoded_address = quote(address)
print(encoded_address)


params = {
    "key": os.environ["GOOGLE_API"],
    "address": encoded_address
}

response = requests.get(voter_url, params = params)
response.status_code
response.json()
print(response.url)


civic_api_key = 
elections_results = elections.elections(civic_api_key)
elections_results
# Make the API request

print(elections_results.json())