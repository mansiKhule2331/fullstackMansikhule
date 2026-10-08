import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, 21, 23, 22, 21],
    "Marks": [85, 78, 92, 74, 88]
}
df = pd.DataFrame(data)
ascending = df.sort_values(by="Marks", ascending=True)
print("Marks in Ascending Order:")
print(ascending)
descending = df.sort_values(by="Marks", ascending=False)
print("\nMarks in Descending Order:")
print(descending)