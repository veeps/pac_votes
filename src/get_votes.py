import requests
import pandas as pd
import xml.etree.ElementTree as ET

def parse_votes(vote_elements, mapping):
    """
    Generic function to parse vote elements based on a given mapping.
    
    Args:
    - vote_elements (list of XML elements): List of vote elements to parse.
    - mapping (dict): Dictionary that maps XML element tags to field names.
    
    Returns:
    - votes (list of dict): Parsed votes with candidate names, states, and positions.
    """
    votes = []
    for vote in vote_elements:
        vote_data = {}
        for key, tag in mapping.items():
            element = vote.find(tag)
            vote_data[key] = element.text.strip() if element is not None else ''
        
        # Handle specific adjustments (e.g., extracting name and state for rollcall)
        if 'CAND_LAST_NAME' in vote_data and '(' in vote_data['CAND_LAST_NAME']:
            name, state = vote_data['CAND_LAST_NAME'].rsplit('(', 1)
            vote_data['CAND_LAST_NAME'] = name.strip()
            vote_data['CAND_OFFICE_ST'] = state.rstrip(')')
        
        # Standardize and append vote record
        votes.append({
            'CAND_LAST_NAME': vote_data.get('CAND_LAST_NAME', '').upper(),
            'CAND_OFFICE_ST': vote_data.get('CAND_OFFICE_ST', ''),
            'CAND_VOTE': vote_data.get('CAND_VOTE', '').lower()
        })
    return votes

def extract_metadata(root, title_tag, date_tag, result_tag):
    """
    Extracts metadata (title, date, and result) from the root XML element.

    Args:
    - root (XML element): Root XML element to extract from.
    - title_tag (str): Tag name for the title.
    - date_tag (str): Tag name for the date.
    - result_tag (str): Tag name for the result.

    Returns:
    - title (str), date (str), result (str): Extracted values for each metadata field.
    """
    title = root.find(f".//{title_tag}").text if root.find(f".//{title_tag}") is not None else ''
    date = root.find(f".//{date_tag}").text if root.find(f".//{date_tag}") is not None else ''
    result = root.find(f".//{result_tag}").text if root.find(f".//{result_tag}") is not None else ''
    return title, date, result

def get_rollcall_votes(url):
    # Fetch and parse the XML file
    response = requests.get(url)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    # URL-based configurations for XML tag mappings and metadata fields
    if "clerk.house.gov" in url:
        vote_elements = root.findall(".//recorded-vote")
        vote_mapping = {'CAND_LAST_NAME': 'legislator', 'CAND_VOTE': 'vote'}
        title_tag, date_tag, result_tag = "vote-desc", "action-date", "vote-result"

    elif "https://www.senate.gov" in url:
        vote_elements = root.findall(".//member")
        vote_mapping = {'CAND_LAST_NAME': 'last_name', 'CAND_OFFICE_ST': 'state', 'CAND_VOTE': 'vote_cast'}
        title_tag, date_tag, result_tag = "vote_question_text", "vote_date", "vote_result_text"

    else:
        raise ValueError(f"Unsupported URL pattern: {url}")

    # Extract votes and metadata
    votes = parse_votes(vote_elements, vote_mapping)
    bill_title, bill_date, vote_result = extract_metadata(root, title_tag, date_tag, result_tag)

    # Create a standardized DataFrame
    df = pd.DataFrame(votes, columns=['CAND_LAST_NAME', 'CAND_OFFICE_ST', 'CAND_VOTE'])
    return bill_title, bill_date, vote_result, df