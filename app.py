from shiny import App, render, ui, reactive
import pandas as pd
import os
import json
import sys

with open('project_config.json','r') as fp: 
    project_config = json.load(fp)
 
module_path = os.path.join(project_config['project_module_relative_path'])
sys.path.append(module_path)
import get_votes
from get_votes import * 
 

############## Read in PAC data
pacs = pd.read_csv("data/pacs.csv")

# Define UI
app_ui = ui.page_fluid(
    ui.h2("Candidate Transaction Summary"),
    ui.input_text("bill_url",label = "Bill voting records", value = "https://clerk.house.gov/evs/2023/roll724.xml" ),
    ui.output_data_frame("grouped_table")
)

# Define server logic
def server(input, output, session):
    @reactive.calc
    def votes():
        # req() stops execution until input.file() is truthy
        votes = get_rollcall_votes(input.bill_url())
        return votes
    
    @reactive.calc
    def grouped_df():
        # Merge on 'CAND_LAST_NAME'
        df = pd.merge(votes(), pacs, on='CAND_LAST_NAME', suffixes=('_v', '_p'), how='left')

        # If 'CAND_ST' in votes is not empty, ensure it matches with 'CAND_ST' in pacs
        df = df[(df['CAND_OFFICE_ST_v']=="") | (df['CAND_OFFICE_ST_v'] == df['CAND_OFFICE_ST_p'])]

        # Drop the extra 'CAND_ST_p' column after ensuring the match
        df.drop(columns=['CAND_OFFICE_ST_v'], inplace = True)

        # Rename column
        df = df.rename(columns={'CAND_ST_p': 'CAND_ST'})

        # Generate summary table
        grouped_df = df[df['CAND_VOTE'] == "yea"].groupby(['CAND_NAME', 'CAND_PTY_AFFILIATION']).agg({'TRANSACTION_AMT': 'sum'}).reset_index().sort_values(by = "TRANSACTION_AMT", ascending = False)

        grouped_df = grouped_df.rename(columns={'CAND_NAME': 'Candidate Name',
                                            'TRANSACTION_AMT': 'Total $ received from insurance PACs 2020-2024',
                                            'CAND_PTY_AFFILIATION': 'Candidate Party'})

        return grouped_df
    
    
    @render.data_frame
    def grouped_table():
        return grouped_df()


# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()

