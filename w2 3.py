import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, np.nan, 95]
})

print("Using fillna()")
print(df.fillna(0))

print("\nUsing dropna()")
print(df.dropna())