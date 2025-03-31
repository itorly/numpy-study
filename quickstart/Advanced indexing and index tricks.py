# 4. Advanced indexing and index tricks
print('\n# 4. Advanced indexing and index tricks')

import numpy as np

# 4.1 Indexing with arrays of indices
print('\n# 4.1 Indexing with arrays of indices')

# 4.1.1
# the indexed array : a single dimensional array
# the dimension of indexes : 1 (It can only be 1)
# the shape of an index : a bidimensional array
print('# 4.1.1')
print('# the indexed array : 1D array')
print('# the dimension of indexes : 1 (It can only be 1)')
print('# the shape of an index : a bidimensional array')
a = np.arange(12)**2  # the first 12 square numbers
print('a =\n', a)
i = np.array([1, 1, 3, 8, 5])  # an array of indices
print('i =', i)
# the elements of `a` at the positions `i`
print('a[i] =', a[i])
j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print('j =\n', j)
# the same shape as `j`
print('a[j] =\n', a[j])
# IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
# print('a[[3, 4], [9, 7]] =\n', a[[3, 4], [9, 7]])



