import pandas as pd

df = pd.DataFrame({
    "price": ["100", "200", "NA", "400"]
})

df["price"] = pd.to_numeric(df["price"], errors="coerce")

print(df["price"].dtype)
print(df["price"].sum())