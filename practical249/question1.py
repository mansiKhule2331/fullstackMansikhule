# Create a Student class
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    # Method to display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name  :", self.name)
        print("Roll No:", self.rollno)
        print("Marks :", self.marks)


# Accept details from the user
name = input("Enter student name: ")
rollno = input("Enter roll number: ")
marks = float(input("Enter marks: "))

# Create object
s1 = Student(name, rollno, marks)

# Display student details
s1.display()