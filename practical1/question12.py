import pandas as pd
# a) Read the CSV file
df = pd.read_csv("employee_data.csv")
# b) Display the complete dataset
print("Complete Dataset:")
print(df)
# c) Check whether the dataset contains missing values
print("\nDoes the dataset contain missing values?")
print(df.isnull().values.any())
# d) Count the number of missing values in each column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# e) Replace missing Age values with the average age
average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)
# f) Replace missing Salary values with 0
df["Salary"] = df["Salary"].fillna(0)
# g) Replace missing Department values with "Not Assigned"
df["Department"] = df["Department"].fillna("Not Assigned")
# h) Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df)
# i) Sort employees according to salary
sorted_df = df.sort_values(by="Salary", ascending=True)
print("\nEmployees Sorted by Salary:")
print(sorted_df)
# j) Save the cleaned data
sorted_df.to_csv("cleaned_employee_data.csv", index=False)
print("\nCleaned data saved successfully as cleaned_employee_data.csv")