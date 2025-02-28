import numpy as np
# Create a 2D array
#arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
# Slice every second row and column
sliced_arr = arr[1:, 2:]
print("Sliced Array with Steps:\n", sliced_arr)

arr_3 = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [1., 3., 5.]])
arr_tranp = arr_3.transpose()
print("Original matrix:\n", arr_3)
print("Transpose matrix:\n", arr_tranp)
# Try:
print(arr_3.shape)
print(arr_3.T)
print(arr_3.T.shape)
