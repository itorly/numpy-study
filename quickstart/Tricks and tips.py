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

