import pandas as pd

df = pd.DataFrame({
    "Price": ["100", "250", "NA", "400"]
})

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print(df)