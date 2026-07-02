import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, 90, None]
})

clean_df = df.dropna()

print("Original DataFrame")
print(df)

print("\nCleaned DataFrame")
print(clean_df)