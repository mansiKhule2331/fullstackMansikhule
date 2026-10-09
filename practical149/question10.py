#conacanate 2D array along columns
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])  
arr2 = np.array([[5, 6], [7, 8]])
concatenated_arr = np.concatenate((arr1, arr2), axis=1)
print("Concatenated array along columns:\n", concatenated_arr)