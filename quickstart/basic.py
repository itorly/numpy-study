import numpy as np
a = np.arange(15).reshape(3, 5)
print('a = ', a)
print('a.shape = ', a.shape)
print('a.ndim = ', a.ndim)
print('a.dtype = ', a.dtype.name)
print('a.dtype.itemsize = ', a.itemsize)
print('a.size = ', a.size)