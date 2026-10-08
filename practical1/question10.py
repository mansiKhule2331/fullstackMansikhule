import pandas as pd
# a) Read the CSV file
df = pd.read_csv("employees.csv")
# b) Display all employees
print("All Employees:")
print(df)
# c) Display employees whose salary is greater than ₹40,000
print("\nEmployees with Salary Greater than 40000:")
print(df[df["Salary"] > 40000])
# d) Find the highest salary
highest_salary = df["Salary"].max()
print("\nHighest Salary:", highest_salary)
# e) Find the lowest salary
lowest_salary = df["Salary"].min()
print("Lowest Salary:", lowest_salary)
# f) Calculate the average salary
average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)
# g) Find average salary of each department
department_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary of Each Department:")
print(department_salary)
# h) Display employees having more than 3 years of experience
print("\nEmployees with More Than 3 Years Experience:")
print(df[df["Experience"] > 3])
# i) Sort employees by salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nEmployees Sorted by Salary (Descending):")
print(sorted_df)
# j) Save the result into employee_analysis.csv
sorted_df.to_csv("employee_analysis.csv", index=False)
print("\nResult saved successfully as employee_analysis.csv")