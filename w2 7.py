import pandas as pd

df = pd.DataFrame({
    "Marks": [80, 90, 95]
})

filtered = df[df["Marks"] > 85].copy()

filtered["Marks"] = filtered["Marks"] + 5

print(filtered)