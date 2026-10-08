import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Maths": [85, 78, 92, 74, 88],
    "Science": [90, 82, 89, 76, 91]
}
df = pd.DataFrame(data)
df["Total"] = df["Maths"] + df["Science"]
print("Student DataFrame:")
print(df)