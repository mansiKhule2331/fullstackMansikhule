#concanates two array along rows
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("Concatenated array along rows:\n", concatenated_arr)