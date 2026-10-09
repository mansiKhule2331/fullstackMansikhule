import math

# Create a Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


# Accept radius from the user
r = float(input("Enter the radius of the circle: "))

# Create object
c1 = Circle(r)

# Display results
print("\n--- Circle Details ---")
print("Radius        :", c1.radius)
print("Area          :", round(c1.area(), 2))
print("Circumference :", round(c1.circumference(), 2))