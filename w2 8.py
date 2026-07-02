import pandas as pd

income = pd.Series([20, 30, 40, 60, 80, 100])

labels = pd.qcut(
    income,
    3,
    labels=["Low", "Mid", "High"]
)

print(labels)