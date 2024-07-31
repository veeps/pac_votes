import pandas

df = pd.read_csv("data/pacs.csv")
df.columns

cvs = df[df["CMTE_ID"] == "C00384818"]
cvs.groupby(["YEAR", "CAND_PTY_AFFILIATION"])["TRANSACTION_AMT"].sum()