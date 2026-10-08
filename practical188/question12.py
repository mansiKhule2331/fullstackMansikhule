def is_armstrong_number(number: int) -> bool:
    """
    Determines whether a given positive integer is an Armstrong number.
    An Armstrong number is equal to the sum of its own digits, 
    each raised to the power of the number of digits.
    """
    # Negative numbers cannot be Armstrong numbers
    if number < 0:
        return False
        
    # Convert the number to a string to easily count digits and iterate
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of total digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the calculated sum matches the original number
    return armstrong_sum == number

# Example Usage
if __name__ == "__main__":
    # Test cases
    test_numbers = [9, 153, 371, 1634, 123]
    
    for num in test_numbers:
        if is_armstrong_number(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is NOT an Armstrong number.")