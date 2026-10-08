def differenceofSum(n, m):
    # Initialize variables to keep track of the sums
    sum_divisible = 0
    sum_not_divisible = 0
    
    # Iterate through all numbers from 1 to m (inclusive)
    for i in range(1, m + 1):
        if i % n == 0:
            sum_divisible += i
        else:
            sum_not_divisible += i
            
    # Return the difference as specified
    return sum_not_divisible - sum_divisible