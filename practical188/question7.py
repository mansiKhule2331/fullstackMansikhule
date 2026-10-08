# Python program to display the multiplication table of a number entered by the user

# Take input from the user
# The input() function reads data as a string, so we convert it to an integer using int()
num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:")

# Use a for loop to iterate from 1 to 10
# range(1, 11) starts at 1 and stops before 11 (meaning it goes up to 10)
for i in range(1, 11):
    result = num * i
    # Display the formatted multiplication expression
    print(f"{num} x {i} = {result}")