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

# eg 2.How does it work?
print("\n# 2.How does it work?")
# Create a 4x5 array
a = np.arange(20).reshape(4, 5)
print("Original array:")
print(a)

# Select specific rows and columns
rows = np.array([0, 2, 3])
cols = np.array([1, 2, 4])

# Use ix_ to create indexing arrays
indices = np.ix_(rows, cols)
result = a[indices]

print("\nSelected sub-array:")
print(result)

# eg 3.Behavior in 3D
print("\n# 3.Behavior in 3D")

b = np.arange(24).reshape(2, 3, 4)
print("Original array:")
print(b)

sub_b = b[np.ix_([0], [1, 2], [0, 3])]  # Shape: (1, 2, 2)
print("\nSelected sub-array:")
print(sub_b)