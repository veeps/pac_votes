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
pacs = pd.read_csv("data/pacs_1995_2024.csv")

# Define UI
app_ui = ui.page_fluid(
    ui.h1("Voting records and $$$ received by insurance PACs"),
    ui.h5("This tool pulls the voting record on congressional bills and traces the amount of money each member has received from the following insurance PACs: Humana, CVS Aetna, Elevance, United Health, HCSC, and Centene from 1995 to 2024. Data was pulled directly from SEC, and voting records from congress.gov", style = "margin-top: 25px; margin-bottom: 25px",),
    ui.row(ui.column(6, "To see the voting records for a bill, add the XML link for the bill you're interested in. Go to https://www.congress.gov and find the bill's roll call number. Click on the XML View from that page and add the link here to view."),
           ui.column(6, ui.input_text("bill_url",label = ui.h5("Enter XML link here"), value = "https://clerk.house.gov/evs/2022/roll360.xml" )), style = "background-color:#1066ff; padding-top:25px; padding-bottom:25px;"

    ),
    ui.row(ui.h3(ui.output_text("bill_title")),
           ui.h5(ui.output_text("vote_result")), style="padding-top: 25px"
           ),
    ui.row(
        ui.column(6, ui.h4("Yes Votes"), ui.output_data_frame("yea_table")),
        ui.column(6, ui.h4("No Votes"), ui.output_data_frame("nay_table"),
                  ui.h4("Abstain", style = "margin-top: 50px"), ui.output_data_frame("abstain_table")), style = "margin-top: 50px"
    ), style = "padding:50px"
)

# Define server logic
def server(input, output, session):

    @render.text
    def bill_title():
        # req() stops execution until input.file() is truthy
        bill_title = get_rollcall_votes(input.bill_url())[0]
        return "Bill Title: " + bill_title

    @render.text
    def vote_result():
        vote_result = get_rollcall_votes(input.bill_url())[2]
        # req() stops execution until input.file() is truthy
        bill_date = get_rollcall_votes(input.bill_url())[1]
        return "This bill was " + vote_result + " on " + bill_date

    @reactive.calc
    def votes():
        # req() stops execution until input.file() is truthy
        votes = get_rollcall_votes(input.bill_url())[3]
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
    
    @reactive.calc
    def abstain_df():
        abstain_df = get_summary_table("not voting", df())
        return abstain_df
    
    
    @render.data_frame
    def yea_table():
        return yea_df()
    
    @render.data_frame
    def nay_table():
        return nay_df()
    
    @render.data_frame
    def abstain_table():
        return abstain_df()


# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()

