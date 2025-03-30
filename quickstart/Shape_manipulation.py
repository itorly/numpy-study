# # # 2.Shape manipulation
print('\n## 2.Shape manipulation')
import numpy as np

# 2.1 Changing the shape of an array
print('\n### 2.1 Changing the shape of an array')

# Parameter 1 is the seed value, which is used to control the reproducibility of random number generation.
rg = np.random.default_rng(1)  # create instance of default random number generator

a = np.floor(10 * rg.random((3, 4)))
print('a =', a)
# a.shape
print('a.shape =', a.shape)

# a.ravel()  # returns the array, flattened
print('a.ravel() =', a.ravel())
# The reshape function returns its argument with a modified shape
# The reshape function returns its argument with a modified shape
# a.reshape(6, 2)  # returns the array with a modified shape
print('a.reshape(6, 2) =', a.reshape(6, 2))
# a.T  # returns the array, transposed
print('a.T =', a.T)
# a.T.shape
print('a.T.shape =', a.T.shape)
# a.shape
print('a.shape =', a.shape)

# the ndarray.resize method modifies the array itself
a.resize((2, 6))
print('a =', a)

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated
# a.reshape(4, -1)
print('a.reshape(4, -1) =', a.reshape(4, -1))


# 2.2 Stacking together different arrays
print('\n### 2.2 Stacking together different arrays')

# Several arrays can be stacked together along different axes
# vstack, hstack
a = np.floor(10 * rg.random((2, 2)))
print('a =\n', a)
b = np.floor(10 * rg.random((2, 2)))
print('b =\n', b)
# np.vstack((a, b))
print('np.vstack((a, b)) =\n', np.vstack((a, b)))
# np.hstack((a, b))
print('np.hstack((a, b)) =\n', np.hstack((a, b)))

# The function column_stack stacks 1D arrays as columns into a 2D array.
# It is equivalent to hstack only for 2D arrays:
from numpy import newaxis

# with 2D arrays
print('np.column_stack((a, b)) =\n', np.column_stack((a, b)))

a = np.array([4., 2.])
b = np.array([3., 8.])
# returns a 2D array
print('np.column_stack((a, b)) =\n', np.column_stack((a, b)))

# 1D arrays
print('np.hstack((a, b)) =\n', np.hstack((a, b)))

# view `a` as a 2D column vector
print('a[:, newaxis] =\n', a[:, newaxis])

# np.column_stack((a[:, newaxis], b[:, newaxis]))
print('np.column_stack((a[:, newaxis], b[:, newaxis])) =\n', np.column_stack((a[:, newaxis], b[:, newaxis])))

# np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same
print('np.hstack((a[:, newaxis], b[:, newaxis])) =\n', np.hstack((a[:, newaxis], b[:, newaxis])))

# In complex cases, r_ and c_ are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals
print('np.r_[0:4, 5, 6] =\n', np.r_[0:4, 5, 6])
print('np.r_[1:4, 0, 4] =\n', np.r_[1:4, 0, 4])