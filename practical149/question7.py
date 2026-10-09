#stack two arrays vertically
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
stacked_arr = np.vstack((arr1, arr2))
print("Stacked array:\n", stacked_arr)