import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, 21, 23, 22, 21],
    "City": ["Kolhapur", "Pune", "Mumbai", "Nashik", "Satara"],
    "Marks": [85, 78, 92, 74, 88]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df = df.drop("City", axis=1)
print("\nDataFrame after deleting City column:")
print(df)