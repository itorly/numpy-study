# 5.Tricks and tips
print('\n# 5.Tricks and tips\n')

import numpy as np

# 5.1 “Automatic” reshaping
print('\n# 5.1 “Automatic” reshaping')

a = np.arange(30)
b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"
# b.shape
print('b.shape =', b.shape)
# b
print('b =\n', b)

# 5.2 Vector stacking
print('\n# 5.2 Vector stacking')

x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x, y])
# m
print('m =\n', m)
xy = np.hstack([x, y])
# xy
print('xy =\n', xy)
