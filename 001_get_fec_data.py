import pandas as pd
import re
import os

############## Function to process data 

def read_and_process_files(regex, header_file):
    # List to hold individual dataframes
    dataframes = []

    # Read in header file
    header = pd.read_csv(header_file)
    
    # Iterate over all files in the data folder
    for filename in os.listdir("data"):
        match = re.search(regex, filename)
        if match:
            year = match.group(1)
            # Read the file into a dataframe
            filepath = os.path.join("data", filename)
            df = pd.read_csv(filepath, sep="|")
            # Add in column headers
            df.columns = header.columns
            # Add the year column
            df["YEAR"] = year.replace("_", "-")
            # Append the dataframe to the list
            dataframes.append(df)
    
    # Concatenate all dataframes into one
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

############## Pull data for committees of interest
insurance_pacs = ["C00271007","C00384818","C00197228","C00274431","C00199711","C00397851"]

############## Read in data files
contributions = read_and_process_files(r"contributions_(\d+_\d+)\.txt", "data/header_contributions.csv")
contributions['YEAR'].unique()

############## Get committee names
cm = pd.read_csv("data/cm_2023_2024.txt", sep = "|")

header = pd.read_csv("data/header_file.csv")
cm.columns = header.columns
pacs = pd.merge(contributions, cm[["CMTE_ID", "CMTE_NM"]], how = "left")
pacs = pacs[pacs["CMTE_ID"].isin(insurance_pacs)]

############## Pull data for candidates
candidates = read_and_process_files(r"cn_(\d+_\d+)\.txt", "data/header_candidates.csv")
candidates.drop(columns = ["YEAR"], inplace = True)
candidates.drop_duplicates(subset = ['CAND_ID'], inplace = True, keep = "first")

############## Merge candidate names
df = pd.merge(pacs, candidates, how  = "left", left_on= "CAND_ID", right_on="CAND_ID")


#### Get last names
df['CAND_LAST_NAME'] = df['CAND_NAME'].str.split(",").str[0]

#### Update to a numeric date
df['YEAR_END'] = df['YEAR'].str.split("-").str[1]
df['YEAR_END'] = df["YEAR_END"].astype(int)

#### Get simplified pac names
names = pd.read_csv("pac_names.csv")
df_names = pd.merge(df, names, how = "left")

#### Write to csv
df_names.to_csv("data/pacs_1995_2024.csv", index = False)

df["YEAR"].unique()
df.shape