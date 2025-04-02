import numpy as np

# ix_(*args) function
print('# ix_(*args) function')

# eg 1. What is it?
print('# 1.What is it?')
# Define 1-D arrays
a = np.array([1, 2, 3])
b = np.array([5, 6])

# Create an open mesh grid
grid = np.ix_(a, b)

print(grid)

