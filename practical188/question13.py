def count_string_elements(input_string):
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    special_count = 0
    
    # Define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")
    
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            # Spaces and symbols are treated as special characters
            special_count += 1
            
    print(f"Original String: {input_string}")
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonants_count}")
    print(f"Digits: {digits_count}")
    print(f"Special Characters: {special_count}")

# Example usage:
user_input = "Python 3.12 @ Learning!"
count_string_elements(user_input)