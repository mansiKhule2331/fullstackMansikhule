import numpy as np
arr=np.array([1, 2, 3, 4, 5])
odds=arr[arr % 2 == 1]
print("Odd numbers in the array:", odds)