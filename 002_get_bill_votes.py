import requests
import xml.etree.ElementTree as ET

# Fetch the XML file from the URL
url = 'https://clerk.house.gov/evs/2023/roll724.xml'
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status codes

# Parse the XML content
root = ET.fromstring(response.content)

# Extract "yea" and "nay" votes with candidate and state
votes = []

for vote in root.findall(".//recorded-vote"):
    legislator_name = vote.find('legislator').text.strip()
    vote_position = vote.find('vote').text.strip().lower()
    
    # Extract candidate name and state
    if '(' in legislator_name and ')' in legislator_name:
        candidate_name, state = legislator_name.rsplit('(', 1)
        state = state.rstrip(')')
    else:
        candidate_name = legislator_name
        state = ''

    # Append to votes list
    votes.append({
        'CAND_LAST_NAME': candidate_name.strip(),
        'CAND_OFFICE_ST': state.strip(),
        'CAND_VOTE': vote_position
    })

# Create a DataFrame from the votes list
df = pd.DataFrame(votes, columns=['CAND_LAST_NAME', 'CAND_OFFICE_ST', 'CAND_VOTE'])