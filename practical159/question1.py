#split an array into 3 parts
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
split_arr = np.array_split(arr, 3)
print("Split array into 3 parts:", split_arr)