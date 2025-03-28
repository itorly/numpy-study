# # An example
# Import the numpy library for numerical operations
import numpy as np

# Create a 1D array with values from 0 to 14 and reshape it into a 3x5 matrix
a = np.arange(15).reshape(3, 5)
print('a = \n', a)

# Print the shape of the array 'a' (rows, columns)
print('a.shape = ', a.shape)

# Print the number of dimensions of the array 'a'
print('a.ndim = ', a.ndim)

# Print the data type of the elements in the array 'a'
print('a.dtype = ', a.dtype.name)

# Print the size in bytes of each element in the array 'a'
print('a.dtype.itemsize = ', a.itemsize)

# Print the total number of elements in the array 'a'
print('a.size = ', a.size)