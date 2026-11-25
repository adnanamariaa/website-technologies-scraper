import pandas as pd
from pathlib import Path

Path("data_out").mkdir(exist_ok=True)

df = pd.read_parquet("data_in/domenii.parquet")
print(df.shape)      
print(df.columns)    

df.to_csv("data_out/rezultate.csv", index=False)

col = df["root_domain"]

print("1. Missing values:", col.isna().sum())
print("2. Empty strings:", (col.str.strip() == "").sum())
print("3. Duplicates:", col.duplicated().sum())
print("4. Unique values:", col.nunique())
print("5. Contains uppercase letters:", (col != col.str.lower()).sum())
print("6. Contains whitespace:", col.str.contains(r"\s", na=False).sum())
print("7. Punycode (xn--):", col.str.contains("xn--", na=False).sum())
print("\n8. Top TLDs:\n", col.str.split(".").str[-1].value_counts().head(15))
print("\n9. Domains with 2+ dots:\n", df[col.str.count(r"\.") >= 2].to_string())