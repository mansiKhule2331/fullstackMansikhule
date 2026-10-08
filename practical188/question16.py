# Functions for basic arithmetic operations

def add(x, y):
    """Returns the sum of two numbers"""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers"""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers"""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers, handling division by zero"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting the program.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Option. Please choose a valid operation.")

if __name__ == "__main__":
    main()