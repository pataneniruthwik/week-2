import pandas as pd

df = pd.DataFrame({
    "name": ["Rahul", "Priya"],
    "age": [22, 21]
})

print(df.loc[0])
print(type(df.loc[0]))