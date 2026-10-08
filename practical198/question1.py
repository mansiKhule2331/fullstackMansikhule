def longest_increasing_subarray(arr):
    if not arr:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
            
    return max(max_length, current_length)

# Reading Sample Input
if __name__ == "__main__":
    n = int(input().strip())
    # Reads either space-separated integers or a contiguous string of single digits
    line = input().strip()
    if ' ' in line:
        arr = list(map(int, line.split()))
    else:
        arr = [int(char) for char in line]
        
    print(longest_increasing_subarray(arr))