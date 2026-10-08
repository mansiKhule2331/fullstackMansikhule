# 1. Store marks of 3 subjects
subject_1 = 85
subject_2 = 90
subject_3 = 78

# 2. Calculate Total and Percentage (assuming max marks per subject is 100)
total_marks = subject_1 + subject_2 + subject_3
percentage = (total_marks / 300) * 100

# 3. Determine Grade based on percentage
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

# Display the results
print(f"Total Marks: {total_marks}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")