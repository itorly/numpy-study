# # An example
# Import the numpy library for numerical operations
import numpy as np

# Create a 1D array with values from 0 to 14 and reshape it into a 3x5 matrix
a = np.arange(15).reshape(3, 5)
print('a =\n', a)

# Print the shape of the array 'a' (rows, columns)
print('a.shape =', a.shape)

# Print the number of dimensions of the array 'a'
print('a.ndim =', a.ndim)

# Print the data type of the elements in the array 'a'
print('a.dtype =', a.dtype.name)

# Print the size in bytes of each element in the array 'a'
print('a.dtype.itemsize =', a.itemsize)

# Print the total number of elements in the array 'a'
print('a.size =', a.size)

# Array creation
# Import the numpy library and alias it as 'np' for convenience
import numpy as np

# Create a one-dimensional NumPy array with integer elements [2, 3, 4]
a = np.array([2, 3, 4])
print('a =', a)
print('a.dtype =', a.dtype)

# Create a one-dimensional NumPy array with floating-point elements [1.2, 3.5, 5.1]
b = np.array([1.2, 3.5, 5.1])
print('b.dtype =', b.dtype)

# Create a two-dimensional NumPy array with mixed-type elements [(1.5, 2, 3), (4, 5, 6)]
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print('b =', b)

# Create a two-dimensional NumPy array with complex numbers [[1, 2], [3, 4]]
c = np.array([[1, 2], [3, 4]], dtype=complex)
print('c =', c)

# Create a two-dimensional array filled with zeros of shape (3, 4)
zeros = np.zeros((3, 4))
print('zeros =\n', zeros)

# Create a three-dimensional array filled with ones of shape (2, 3, 4) and data type int16
ones = np.ones((2, 3, 4), dtype=np.int16)
print('ones =\n', ones)

# Create a two-dimensional uninitialized array of shape (2, 3), with arbitrary values depending on memory state
empty = np.empty((2, 3))
print('empty =\n', empty)

arange = np.arange(10, 30, 5)
print('arange =', arange)

# it accepts float arguments
# When arange is used with floating point arguments,
# it is generally not possible to predict the number of elements obtained,
# due to the finite floating point precision.
np_arange = np.arange(0, 2, 0.3)
print('np_arange =', np_arange)

from numpy import pi
# 9 numbers from 0 to 2
linspace = np.linspace(0, 2, 9)
print('linspace =', linspace)

# 6 numbers from 0 to 2*pi, useful to evaluate function at lots of points
x = np.linspace(0, 2 * pi, 6)        # useful to evaluate function at lots of points
print('x =', x)

# Compute the sine of each element in the array x
f = np.sin(x)
print('f =', f)
