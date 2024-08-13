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
import get_summary_table
from get_votes import * 
from get_summary_table import * 
 

############## Read in PAC data
pacs = pd.read_csv("data/pacs.csv")

# Define UI
app_ui = ui.page_fluid(
    ui.h2("Candidate Transaction Summary"),
    ui.input_text("bill_url",label = "Bill voting records", value = "https://clerk.house.gov/evs/2023/roll724.xml" ),
    ui.row(
        ui.column(6, ui.output_data_frame("yea_table")),
        ui.column(6, ui.output_data_frame("nay_table"))
    )
)

# Define server logic
def server(input, output, session):
    @reactive.calc
    def votes():
        # req() stops execution until input.file() is truthy
        votes = get_rollcall_votes(input.bill_url())
        return votes
    
    @reactive.calc
    def df():
        # Merge on 'CAND_LAST_NAME'
        df = pd.merge(votes(), pacs, on='CAND_LAST_NAME', suffixes=('_v', '_p'), how='left')

        # If 'CAND_ST' in votes is not empty, ensure it matches with 'CAND_ST' in pacs
        df = df[(df['CAND_OFFICE_ST_v']=="") | (df['CAND_OFFICE_ST_v'] == df['CAND_OFFICE_ST_p'])]

        # Drop the extra 'CAND_ST_p' column after ensuring the match
        df.drop(columns=['CAND_OFFICE_ST_v'], inplace = True)

        # Rename column
        df = df.rename(columns={'CAND_ST_p': 'CAND_ST'})

        return df
    
    @reactive.calc
    def yea_df():
        yea_df = get_summary_table("yea", df())
        return yea_df
    
    @reactive.calc
    def nay_df():
        nay_df = get_summary_table("nay", df())
        return nay_df
    
    
    @render.data_frame
    def yea_table():
        return yea_df()
    
    @render.data_frame
    def nay_table():
        return nay_df()


# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()

