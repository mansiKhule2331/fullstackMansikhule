import pandas as pd
data = {
    "Name": ["Mansi", "Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [85, 65, 92, 58, 78]
}
df = pd.DataFrame(data)
result = df[df["Marks"] > 70]
print("Students who scored more than 70 marks:")
print(result)