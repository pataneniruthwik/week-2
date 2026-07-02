import pandas as pd

df = pd.DataFrame({
    "a": [1, 2, 3, 4]
})

result = df["a"].apply(lambda x: x**2 if x > 2 else "small")

print(result)
print(result.dtype)