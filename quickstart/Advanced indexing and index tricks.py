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

# 4.1.3
# the indexed array : a multidimensional array
# the dimension of indexes : more than one dimension
# the shape of an index : a bidimensional array
print('# 4.1.3')
print('# the indexed array : a multidimensional array')
print('# the dimension of indexes : more than one dimension')
print('# the shape of an index : a bidimensional array')

# We can also give indexes for more than one dimension.
# The arrays of indices for each dimension must have the same shape.
a = np.arange(12).reshape(3, 4)
print('a =\n', a)

i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
# a[i, j]  # i and j must have equal shape
print('a[i, j] =\n', a[i, j])
# a[i, 2]
print('a[i, 2] =\n', a[i, 2])
# a[:, j]
print('a[:, j] =\n', a[:, j])

# 4.1.4 use tuple to index
print('# 4.1.4 use tuple to index')

# arr[i, j] is exactly the same as arr[(i, j)]
l = (i, j)
# equivalent to a[i, j]
# a[l]
print('a[l] =\n', a[l])

# 4.1.5 a case that cannot do the indexing
print('# 4.1.5 a case that cannot do the indexing')
# We can not do this by putting i and j into an array,
# because this array will be interpreted as indexing the first dimension of a.
s = np.array([i, j])
print('s =\n', s)
# not what we want
# a[s]
# same as `a[i, j]`
# a[tuple(s)]
print('a[tuple(s)] =\n', a[tuple(s)])

# 4.1.6 the search of the maximum value of time-dependent series
print('\n# 4.1.6 the search of the maximum value of time-dependent series')

time = np.linspace(20, 145, 5)  # time scale
data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
# time
print('time =', time)
# data
print('data =\n', data)
# index of the maxima for each series
ind = data.argmax(axis=0)
# ind
print('ind =', ind)
# times corresponding to the maxima
time_max = time[ind]
print('time_max =', time_max)

shape_0 = data.shape[0]
shape_1 = data.shape[1]

r = range(shape_1)

data_max = data[ind, r]  # => data[ind[0], 0], data[ind[1], 1]...
# data_max
print('data_max =', data_max)
# np.all(data_max == data.max(axis=0))
print('np.all(data_max == data.max(axis=0)) =', np.all(data_max == data.max(axis=0)))

# 4.1.7 use indexing with arrays as a target to assign to
a = np.arange(5)
# array([0, 1, 2, 3, 4])
a[[1, 3, 4]] = 0
# array([0, 0, 2, 0, 0])

a = np.arange(5)
a[[0, 0, 2]] = [1, 2, 3]
# array([2, 1, 3, 3, 4])

a = np.arange(5)
a[[0, 0, 2]] += 1
# array([1, 1, 3, 3, 4])
