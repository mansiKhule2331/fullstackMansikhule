# Program to store student details using a dictionary and display key-value pairs

# 1. Store student details in a dictionary
student_details = {
    "Roll Number": "A101",
    "Name": "Aman Sharma",
    "Age": 20,
    "Course": "Computer Science",
    "Grade": "A"
}

# 2. Display all key-value pairs using a for loop and .items()
print("--- Student Details ---")
for key, value in student_details.items():
    print(f"{key}: {value}")