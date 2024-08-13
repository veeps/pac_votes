import requests
import pandas as pd
import xml.etree.ElementTree as ET


def get_rollcall_votes(url):
    # Fetch the XML file from the URL
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
    df['CAND_LAST_NAME'] = df['CAND_LAST_NAME'].str.upper()

    # Find the "bill title" 
    bill_title = root.find(".//vote-desc").text

    # Find the "bill date" 
    bill_date = root.find(".//action-date").text

    # Find the "vote result" 
    vote_result = root.find(".//vote-result").text

    return bill_title, bill_date, vote_result, df