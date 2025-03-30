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


