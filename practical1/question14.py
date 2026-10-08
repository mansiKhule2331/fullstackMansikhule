import pandas as pd
# Create DataFrame
data = {
    "Name": [
        "Mansi", "Rahul", "Priya", "Amit", "Sneha",
        "Rohit", "Pooja", "Akash", "Neha", "Karan"
    ],
    "Department": [
        "IT", "HR", "Finance", "IT", "Marketing",
        "Finance", "IT", "HR", "Marketing", "Finance"
    ],
    "Salary": [
        55000, 42000, 48000, 65000, 39000,
        52000, 45000, 37000, 41000, 60000
    ],
    "Experience": [
        3, 5, 4, 6, 2,
        7, 4, 2, 5, 8
    ],
    "City": [
        "Pune", "Mumbai", "Pune", "Kolhapur", "Mumbai",
        "Pune", "Kolhapur", "Pune", "Mumbai", "Kolhapur"
    ]
}
df = pd.DataFrame(data)
print("Complete DataFrame:")
print(df)
# Display complete DataFrame
print("Complete DataFrame:")
print(df)
# a) Display employees with salary > ₹50,000
print("\nEmployees with Salary Greater Than 50000:")
print(df[df["Salary"] > 50000])
# b) Find average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)
# c) Find highest salary
highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)
# d) Find employees with more than 3 years of experience
print("\nEmployees with More Than 3 Years Experience:")
print(df[df["Experience"] > 3])
# e) Count employees city-wise
print("\nCity-wise Employee Count:")
print(df.groupby("City").size())
# f) Calculate average salary department-wise
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
# g) Sort employees by salary
sorted_df = df.sort_values(by="Salary", ascending=True)
print("\nEmployees Sorted by Salary:")
print(sorted_df)
# h) Save final DataFrame as CSV
sorted_df.to_csv("department_analysis.csv", index=False)
print("\nData saved successfully as department_analysis.csv")