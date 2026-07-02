import pandas as pd

# Series
marks = pd.Series([85, 90, 95])

print("Series:")
print(marks.head())

# DataFrame
students = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, 90, 95]
})

print("\nDataFrame:")
print(students.head())

# DataFrame-only operation
print("\nGroupBy:")
print(students.groupby("Marks").count())