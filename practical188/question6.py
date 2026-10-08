# Python program to calculate total marks, percentage, and grade for 5 subjects

# 1. Accept marks for five subjects from the user
print("Enter the marks obtained out of 100:")
subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

# 2. Calculate Total Marks and Percentage
# Assuming maximum marks for each subject is 100, so total maximum marks = 500
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

# 3. Determine Grade based on the percentage criteria
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F (Fail)"

# 4. Display the results
print("\n--- Results Summary ---")
print(f"Total Marks Scored: {total_marks} / 500")
print(f"Percentage:         {percentage:.2f}%")
print(f"Assigned Grade:     {grade}")