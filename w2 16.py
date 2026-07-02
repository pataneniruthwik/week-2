import pandas as pd

df = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [10, 20, 30]
})

print(df[df["a"] > 1])

# Wrong
# print(df[df["a"] > 1 & df["b"] > 15])

# Correct
print(df[(df["a"] > 1) & (df["b"] > 15)])