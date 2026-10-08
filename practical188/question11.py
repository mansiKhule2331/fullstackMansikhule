def reverse_and_check_palindrome(number):
    # Store the original number to compare later
    original_num = number
    reversed_num = 0
    
    # Mathematical logic to reverse the number
    while number > 0:
        remainder = number % 10
        reversed_num = (reversed_num * 10) + remainder
        number = number // 10
        
    print(f"Original Number: {original_num}")
    print(f"Reversed Number: {reversed_num}")
    
    # Check if the number is a palindrome
    if original_num == reversed_num:
        print("Result: The number is a palindrome!")
    else:
        print("Result: The number is NOT a palindrome.")

# Example Usage
user_input = 12321
reverse_and_check_palindrome(user_input)