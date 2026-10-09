class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("\n--- Employee Details ---")
        print("Name          :", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary :", self.salary * 12)


# Accept employee details
name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))

# Create object
e1 = Employee(name, salary)

# Display employee details
e1.display()