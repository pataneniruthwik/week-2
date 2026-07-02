import pandas as pd

df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6]
})

df2 = df

df2["a"] = [10, 20, 30]

print(df)