import numpy as np
arr=np.array([1,2,3,4,5])
even=arr[arr % 2 == 0]
print("Even numbers in the array:", even)