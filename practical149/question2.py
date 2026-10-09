import numpy as np
arr=np.array([1,2,3,4,5])
new_arr=np.where(arr>3,-1,arr)
print("New array with elements greater than 3 replaced by -1:", new_arr)