from shiny import App, render, ui

import pandas as pd
#from datatable import DataTable

# Sample data
data = {
    'CMTE_NM': [
        'DUKE ENERGY CORPORATION PAC', 'THE HOME DEPOT INC. POLITICAL ACTION COMMITTEE',
        'INTERNATIONAL ASSOCIATION OF SHEET METAL, AIR,...'
    ],
    'CAND_NAME': ['ADAMS, ALMA SHEALEY', 'ADAMS, ALMA SHEALEY', 'ADAMS, ALMA SHEALEY'],
    'TRANSACTION_AMT': [1000.0, 5000.0, 2500.0],
    'CAND_VOTE': ['yea', 'yea', 'yea']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define UI
app_ui = ui.page_fluid(
    ui.h2("Candidate Transaction Summary"),
    ui.output_data_frame("grouped_table")
)

# Define server logic
def server(input, output, session):
    # Group by candidate name and vote, and sum the transaction amounts
   
    @render.data_frame
    def grouped_table():
        grouped_df = df.groupby(['CAND_NAME', 'CAND_VOTE']).agg({'TRANSACTION_AMT': 'sum'}).reset_index()
        return grouped_df


# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()

