#Computation Time Comparison: -1
#Python List vs. NumPy Array Computation Speed
import numpy as np
import sys, time
size = 10**6 # Define the size of the list/array
numpy_array = np.arange(size) # NumPy array
python_list = list(range(size)) # Python list
# Using NumPy
start = time.time()
numpy_array + 10 # Element-wise addition
end = time.time()
print("NumPy time:", end - start)
# Using Python List
start = time.time()
python_list = [x + 10 for x in python_list] # List comprehension
end = time.time()
print("Python list time:", end - start)
