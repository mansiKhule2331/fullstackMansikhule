import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, 21, 23, 22, 21],
    "Marks": [85, 78, 92, 74, 88]
}
df = pd.DataFrame(data)
print("Student DataFrame:")
print(df)
print("\nName Column:")
print(df["Name"])
print("\nFirst 3 Rows:")
print(df.head(3))
print("\nLast 2 Rows:")
print(df.tail(2))