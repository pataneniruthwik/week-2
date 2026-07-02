import pandas as pd

df = pd.DataFrame({
    "city": ["Delhi", "Mumbai", "Delhi", "Bengaluru", None]
})

print(df["city"].nunique())
print(len(df["city"].unique()))
print(df["city"].value_counts())