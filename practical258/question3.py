def findCount(length, arr, num, diff):
    count = 0
    
    # Iterate through each element in the array
    for i in range(length):
        # Check if the absolute difference is less than or equal to 'diff'
        if abs(arr[i] - num) <= diff:
            count += 1
            
    # Return count if elements were found, otherwise return -1
    return count if count > 0 else -1

# --- Driver Code to test the function ---
if __name__ == "__main__":
    # Test Input
    arr = [12, 3, 14, 56, 77, 13]
    length = len(arr)
    num = 13
    diff = 2
    
    # Function Call
    result = findCount(length, arr, num, diff)
    print(result)  # Output: 3