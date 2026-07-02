import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, 90, 95]
}, index=[101, 102, 103])

print("Using .loc")
print(df.loc[101])

print("\nUsing .iloc")
print(df.iloc[0])