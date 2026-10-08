import pandas as pd
# a) Read the CSV file
df = pd.read_csv("placement.csv")
# b) Display all student records
print("All Student Records:")
print(df)
# c) Display only selected students
selected = df[df["Status"] == "Selected"]
print("\nSelected Students:")
print(selected)
# d) Count the total number of selected students
total_selected = len(selected)
print("\nTotal Number of Selected Students:", total_selected)
# e) Find the highest package
highest_package = df["Package"].max()
print("Highest Package:", highest_package, "LPA")
# f) Find the lowest package among selected students
lowest_selected_package = selected["Package"].min()
print("Lowest Package Among Selected Students:",
      lowest_selected_package, "LPA")
# g) Calculate the average package of selected students
average_selected_package = selected["Package"].mean()
print("Average Package of Selected Students:",
      round(average_selected_package, 2), "LPA")
# h) Display students having a package greater than 4 LPA
print("\nStudents Having Package Greater Than 4 LPA:")
print(df[df["Package"] > 4])
# i) Sort selected students according to package in descending order
sorted_selected = selected.sort_values(
    by="Package",
    ascending=False
)
print("\nSelected Students Sorted by Package:")
print(sorted_selected)
# j) Find number of students selected by each company
company_count = selected.groupby("Company").size()
print("\nNumber of Students Selected by Each Company:")
print(company_count)
# k) Save selected-student data into selected_students.csv
selected.to_csv("selected_students.csv", index=False)
print("\nSelected student data saved successfully as selected_students.csv")