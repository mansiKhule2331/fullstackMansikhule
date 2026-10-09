# python code for the above approach:

def make_number_odd(n):
    cost = 0

    # For calculating the cost for making the number odd
    while n % 2 != 1 and n > 0:
        # While loop till the number becomes odd
        n //= 10

        # The last digit is even, so we remove it to check the next digit
        # and increment the cost by one.
        cost += 1

    if n == 0 or n % 2 == 0:
        # Return -1 if we cannot make the current number odd
        return -1

    return cost


def make_array_odd(arr):
    min_cost = 0
    for i in range(len(arr)):
        cost = make_number_odd(arr[i])

        # Function call for make_number_odd function
        if cost != -1:
            min_cost += min(3, cost)
        else:
            # If the current element cannot be converted into an odd number,
            # this means we have to delete the current element, which costs 3.
            min_cost += 3

    return min_cost


# Driver's code
arr = [72, 46, 15, 120, 5680]

# Function call
print(make_array_odd(arr))