import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, 21, 23, 22, 21],
    "Marks": [85, 78, 92, 74, 88]
}
df = pd.DataFrame(data)
# Display the DataFrame
print("Student DataFrame:")
print(df)