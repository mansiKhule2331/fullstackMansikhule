# Program to generate the Fibonacci series up to N terms

# Take input from the user
n_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for _ in range(n_terms):
        print(a, end=" ")
        # Update the values for the next term
        a, b = b, a + b