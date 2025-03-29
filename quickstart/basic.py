# # 1.An example
# Import the numpy library for numerical operations
import sys

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

# # 2.Array creation
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



# # 3.Printing arrays
a = np.arange(6)                    # 1d array
print(a)
b = np.arange(12).reshape(4, 3)     # 2d array
print(b)
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)

# If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners
print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))
# To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported


# # 4.Basic operations
print('\n## 4.Basic operations')
# 4.1 Arithmetic operators
print('\n# 4.1 Arithmetic operators')
# Arithmetic operators on arrays apply elementwise.

a = np.array([20, 30, 40, 50])
print('a =', a)
b = np.arange(4)
print('b =', b)
c = a - b
print('c =', c)
# b**2
print('b**2 =', b ** 2)
# 10 * np.sin(a)
print('10 * np.sin(a) =', 10 * np.sin(a))
# a < 35
print('a < 35 =', a < 35)

# 4.2 elementwise product, matrix product
print('\n# 4.2 elementwise product, matrix product')
# the product operator * operates elementwise in NumPy arrays.
# The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
# A * B     # elementwise product
# A @ B     # matrix product
# A.dot(B)  # another matrix product
print('A * B =\n', A * B)
print('A @ B =\n', A @ B)
print('A.dot(B) =\n', A.dot(B))

# 4.3 += and *=, modify an existing array rather than create
print('\n# 4.3 += and *=, modify an existing array rather than create')
# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
rg = np.random.default_rng(1)  # create instance of default random number generator
print('rg =', rg)
a = np.ones((2, 3), dtype=int)
print('a =', a)
b = rg.random((2, 3))
print('b =', b)

a *= 3
print('After a *= 3, a=\n', a)
b += a
print('After b += a, b=\n', b)
# a += b  # b is not automatically converted to integer type
# numpy._core._exceptions._UFuncOutputCastingError
# print('After a += b, a=\n', a)

# 4.4 upcasting
print('\n# 4.4 upcasting')
# When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
a = np.ones(3, dtype=np.int32)
print('a =', a)

b = np.linspace(0, pi, 3)
print('b =', b)
print('b.dtype.name =', b.dtype.name)

c = a + b
print('After c = a + b, c =', c)
print('c.dtype.name =', c.dtype.name)

d = np.exp(c * 1j)
print('After d = np.exp(c * 1j), d =', d)
print('d.dtype.name =', d.dtype.name)

# 4.5 ndarray
print('\n# 4.5 ndarray')
# Many unary operations, such as computing the sum of all the elements in the array
a = rg.random((2, 3))
print('a =', a)

print('a.sum() =', a.sum())
print('a.min() =', a.min())
print('a.max() =', a.max())

# 4.6 an operation along the specified axis of an array
print('\n# 4.6 an operation along the specified axis of an array')
# apply an operation along the specified axis of an array by specifying the axis parameter
b = np.arange(12).reshape(3, 4)
print('b =', b)

# sum of each column
print('b.sum(axis=0) =', b.sum(axis=0))
# sum of each row
print('b.sum(axis=1) =', b.sum(axis=1))
# min of each row
print('b.min(axis=1) =', b.min(axis=1))
# cumulative sum along each row
print('b.cumsum(axis=1) =\n', b.cumsum(axis=1))

# # 5.Universal functions
print('\n## 5.Universal functions')
B = np.arange(3)
print('B =', B)
# np.exp(B)
print('np.exp(B) =', np.exp(B))
# np.sqrt(B)
print('np.sqrt(B) =', np.sqrt(B))
# C = np.array([2., -1., 4.])
C = np.array([2., -1., 4.])
# np.add(B, C)
print('np.add(B, C) =', np.add(B, C))
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, invert, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

# # 6.Indexing, slicing and iterating
print('\n## 6.Indexing, slicing and iterating')
# 6.1 One-dimensional
print('\n## 6.1 One-dimensional')
a = np.arange(10)**3
print('a =', a)
# a[2]
print('a[2] =', a[2])
# a[2:5]
print('a[2:5] =', a[2:5])

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000
print('a =', a)
# a[::-1]  # reversed a
print('a[::-1] =', a[::-1])
for i in a:
    print(i**(1 / 3.))

# 6.2 Multidimensional
print('\n## 6.2 Multidimensional')
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print('b =', b)

# b[2, 3]
print('b[2, 3] =', b[2, 3])
# b[0:5, 1]  # each row in the second column of b
print('b[0:5, 1] =', b[0:5, 1])
# b[:, 1]  # equivalent to the previous example
print('b[:, 1] =', b[:, 1])
# b[1:3, :]  # each column in the second and third row of b
print('b[1:3, :] =', b[1:3, :])
