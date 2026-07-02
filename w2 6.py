import pandas as pd

grades = pd.Series(["A", "B", "A", "C"])

print("Using map()")
print(grades.map({
    "A": "Excellent",
    "B": "Good",
    "C": "Average"
}))

print("\nUsing apply()")
print(grades.apply(lambda x: x.lower()))

print("\nUsing replace()")
print(grades.replace("A", "Outstanding"))