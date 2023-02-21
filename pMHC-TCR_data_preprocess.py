import pandas as pd

file_path = '/home/wuxinchao/data/project/data/seqData/TCR-pMHC_Info_20230220.xlsx'
df = pd.read_excel(file_path)
df = df[["Class", "cellname", "NeoAA", "chain", "HLA", "aaSeqCDR1", "aaSeqCDR2", "aaSeqCDR3"]]

df = df.set_index(['cellname', "chain"])
# extract the NeoAA, HLA, and aaSeqCDR columns
df = df[["NeoAA", "HLA", "aaSeqCDR1", "aaSeqCDR2", "aaSeqCDR3", "Class"]]
df["aaSeqCDR"] = df[df.columns[2:-1]].apply(
    lambda x: '_'.join(x.dropna().astype(str)),
    axis=1
)

idx = pd.IndexSlice

df_a = df.loc[idx[:,"TRA"],]
df_a["AseqCDR"] = df_a["aaSeqCDR"]
df_a.drop(columns=["aaSeqCDR","aaSeqCDR1","aaSeqCDR2","aaSeqCDR3"], inplace=True)
# drop the chain index
df_a.index = df_a.index.droplevel(1)
df_b = df.loc[idx[:,"TRB"],]
df_b["BseqCDR"] = df_b["aaSeqCDR"]
df_b.drop(columns=["aaSeqCDR","aaSeqCDR1","aaSeqCDR2","aaSeqCDR3"], inplace=True)
# drop the chain index
df_b.index = df_b.index.droplevel(1)

# merge the TRA and TRB dataframes by cellname, HLAs, and NeoAA
df_ab = pd.merge(df_a, df_b, on=["cellname", "HLA", "NeoAA", "Class"])

df = df_ab

df["Neo"] = df["NeoAA"].str.slice(0,3) + "_" + df["NeoAA"].str.slice(-4,-1)
df.drop(columns=["NeoAA"], inplace=True)
for chain in ["AseqCDR", "BseqCDR"]:
    df[chain+"_1"] = df[chain].str.split("_").str[0]
    df[chain+"_2"] = df[chain].str.split("_").str[1]
    df[chain+"_3"] = df[chain].str.split("_").str[2]
    df.drop(columns=[chain], inplace=True)


df.to_csv("/home/wuxinchao/data/project/data/seqData/TCR-pMHC_Info_20230220.csv")