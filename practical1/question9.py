import pandas as pd
"""data = {
    "RollNo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": [
        "Mansi", "Rahul", "Priya", "Amit", "Sneha",
        "Rohit", "Pooja", "Akash", "Neha", "Karan"
    ],
    "Python": [85, 78, 92, 67, 88, 74, 95, 81, 69, 90],
    "Java": [82, 75, 89, 70, 91, 79, 93, 85, 72, 88],
    "DBMS": [88, 80, 94, 65, 86, 82, 96, 78, 75, 92]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("students.csv file created successfully!")
print("\nStudent Data:")
print(df)"""
#a)complete database
#print(df)
"""print("\nb) First 5 Records:")
print(df.head(5))"""
# c) Calculate Total Marks
df = pd.read_csv("students.csv")
df["Total Marks"] = df["Python"] + df["Java"] + df["DBMS"]
print("\nc) Total Marks:")
print(df[["RollNo", "Name", "Total Marks"]])
# d) Calculate Percentage
df["Percentage"] = df["Total Marks"] / 3
print("\nd) Percentage:")
print(df[["RollNo", "Name", "Percentage"]])
# e) Add Result column
df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail")
print("\ne) Result:")
print(df[["RollNo", "Name", "Percentage", "Result"]])
# f) Find the student with the highest percentage
highest = df.loc[df["Percentage"].idxmax()]
print("\nf) Student with Highest Percentage:")
print(highest[["RollNo", "Name", "Percentage"]])
# g) Find the average percentage
average_percentage = df["Percentage"].mean()
print("\ng) Average Percentage:")
print(round(average_percentage, 2))
# h) Display students who scored more than 75%
above_75 = df[df["Percentage"] > 75]
print("\nh) Students scoring more than 75%:")
print(above_75[["RollNo", "Name", "Percentage"]])
# i) Sort students by percentage in descending order
sorted_df = df.sort_values(by="Percentage", ascending=False)
print("\ni) Students sorted by Percentage:")
print(sorted_df[["RollNo", "Name", "Percentage", "Result"]])
# j) Save updated data into student_result.csv
df.to_csv("student_result.csv", index=False)
print("\nj) Updated data saved successfully as student_result.csv")