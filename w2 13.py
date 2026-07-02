import pandas as pd

df = pd.DataFrame({
    "rating": [4.5, 3.8, 4.2, 5.0]
})

df_filtered = df[df["rating"] > 4]

df_filtered["rating"] = df_filtered["rating"] * 2

print(df)
print(df_filtered)