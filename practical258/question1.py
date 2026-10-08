def find_count(arr, length, num, diff):
    # Check for empty array or invalid length
    if length <= 0 or arr is None:
        return -1
    
    count = 0
    for i in range(length):
        if abs(arr[i] - num) <= diff:
            count += 1
            
    return count if count > 0 else -1

# Example usage:
arr = [12, 3, 14, 56, 77, 13]
num = 13
diff = 2
print(find_count(arr, len(arr), num, diff))  