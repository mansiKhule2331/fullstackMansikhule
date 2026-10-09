#stack two arrays horizontally
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
stacked_arr = np.hstack((arr1, arr2))
print("Stacked array:\n", stacked_arr)