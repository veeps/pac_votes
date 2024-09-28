import pandas as pd


def get_summary_table(vote, df):
    # Generate summary table
    grouped_df = df[df['CAND_VOTE'] == vote].groupby(['CAND_NAME', 'CAND_PTY_AFFILIATION']).agg({'TRANSACTION_AMT': 'sum'}).reset_index().sort_values(by = "TRANSACTION_AMT", ascending = False)
    grouped_df = grouped_df.rename(columns={'CAND_NAME': 'Candidate Name',
                                            'TRANSACTION_AMT': 'Total $ received from insurance PACs 1995-2024',
                                            'CAND_PTY_AFFILIATION': 'Candidate Party'})
    return grouped_df