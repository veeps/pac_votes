import pandas as pd
import os
import json
import sys
import get_votes
from importlib import reload
from get_votes import * 

with open('project_config.json','r') as fp: 
    project_config = json.load(fp)
 
module_path = os.path.join(project_config['project_module_relative_path'])
sys.path.append(module_path)
 
reload(get_votes)


############## Read in votes for bill
votes = get_rollcall_votes("https://clerk.house.gov/evs/2023/roll724.xml")

############## Read in PAC data
pacs = pd.read_csv("data/pacs.csv")

# Merge on 'CAND_LAST_NAME'
df = pd.merge(votes, pacs, on='CAND_LAST_NAME', suffixes=('_v', '_p'), how='left')
df.shape

# If 'CAND_ST' in votes is not empty, ensure it matches with 'CAND_ST' in pacs
df = df[(df['CAND_OFFICE_ST_v']=="") | (df['CAND_OFFICE_ST_v'] == df['CAND_OFFICE_ST_p'])]

# Drop the extra 'CAND_ST_p' column after ensuring the match
df.drop(columns=['CAND_OFFICE_ST_v'])

# Rename column
df = df.rename(columns={'CAND_ST_p': 'CAND_ST'})