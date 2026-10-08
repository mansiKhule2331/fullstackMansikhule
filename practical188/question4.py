# Python program to determine whether a given number is even or odd

# Take integer input from the user
num = int(input("Enter a number: "))
# A number is even if it is perfectly divisible by 2 (remainder is 0)
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")