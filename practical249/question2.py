class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Accept input from the user
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Create object
r1 = Rectangle(length, breadth)

# Display results
print("\n--- Rectangle Details ---")
print("Length    :", r1.length)
print("Breadth   :", r1.breadth)
print("Area      :", r1.area())
print("Perimeter :", r1.perimeter())