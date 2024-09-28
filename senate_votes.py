import requests
import pandas as pd
import xml.etree.ElementTree as ET


response = requests.get("https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00065.xml")
response.raise_for_status()  # Raise an error for bad status codes

# Parse the XML content
root = ET.fromstring(response.content)

# Extract "yea" and "nay" votes with candidate and state
votes = []

for vote in root.findall(".//member"):
    first_name = vote.find('first_name').text.strip()
    last_name = vote.find('last_name').text.strip()
    party = vote.find('party').text.strip()
    state = vote.find('state').text.strip()
    vote_position = vote.find('vote_cast').text.strip().lower()        

     # Append to votes list
    votes.append({
        'CAND_LAST_NAME': last_name,
        'CAND_OFFICE_ST': state,
        'CAND_VOTE': vote_position
        })

    # Create a DataFrame from the votes list
    votes_df = pd.DataFrame(votes, columns=['CAND_LAST_NAME', 'CAND_OFFICE_ST', 'CAND_VOTE'])
    votes_df['CAND_LAST_NAME'] = votes_df['CAND_LAST_NAME'].str.upper()



df.head()
pacs = pd.read_csv("data/pacs_1995_2024.csv")


df = pd.merge(votes_df, pacs, on='CAND_LAST_NAME', suffixes=('_v', '_p'), how='left')

# If 'CAND_ST' in votes is not empty, ensure it matches with 'CAND_ST' in pacs
df = df[(df['CAND_OFFICE_ST_v']=="") | (df['CAND_OFFICE_ST_v'] == df['CAND_OFFICE_ST_p'])]

# Drop the extra 'CAND_ST_p' column after ensuring the match
df.drop(columns=['CAND_OFFICE_ST_v'], inplace = True)

df.head()