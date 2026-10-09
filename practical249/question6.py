class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Division by zero is not possible"
        return self.a / self.b


# Accept input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Create an object
c = Calculator(num1, num2)

# Display results
print("Addition:", c.addition())
print("Subtraction:", c.subtraction())
print("Multiplication:", c.multiplication())
print("Division:", c.division())