import requests
import xml.etree.ElementTree as ET

# Fetch the XML file from the URL
url = 'https://clerk.house.gov/evs/2023/roll724.xml'
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status codes

# Parse the XML content
root = ET.fromstring(response.content)

# Extract "yea" and "nay" votes
yeas = []
nays = []
abstain = []

for vote in root.findall(".//recorded-vote"):
    legislator_name = vote.find('legislator').text.strip()
    vote_position = vote.find('vote').text.strip().lower()

    if vote_position == 'yea':
        yeas.append(legislator_name)
    elif vote_position == 'nay':
        nays.append(legislator_name)
    elif vote_position == 'not voting':
        abstain.append(legislator_name)

# Print the results
print("Yeas:", yeas)
print("Nays:", nays)

len(abstain)