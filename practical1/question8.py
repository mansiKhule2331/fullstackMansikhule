import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, 21, None, 22, 21],
    "Marks": [85, None, 92, None, 88]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nMissing Values:")
print(df.isnull())
print("\nNumber of Missing Values:")
print(df.isnull().sum())
df["Marks"] = df["Marks"].fillna(0)
print("\nDataFrame after replacing missing Marks with 0:")
print(df)