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

# 4.1.2
# the indexed array : a multidimensional array
# the dimension of indexes : 1
# the shape of an index : a bidimensional array
print('# 4.1.2')
print('# the indexed array : a multidimensional array')
print('# the dimension of indexes : 1')
print('# the shape of an index : a bidimensional array')

# When the indexed array a is multidimensional,
# a single array of indices refers to the first dimension of a.
palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
# the (2, 4, 3) color image
print('palette[image] =\n', palette[image])



