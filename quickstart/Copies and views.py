# 3. Copies and views
print('\n# 3. Copies and views')
import numpy as np

# 3.1 No copy at all
print('\n# 3.1 No copy at all')
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b = a            # no new object is created
b is a           # a and b are two names for the same ndarray object
print('b is a:', b is a)

def f(x):
    print(id(x))

# id is a unique identifier of an object
print('id(a) =', id(a))

# may vary
f(a)


# 3.2 View or shallow copy
print('\n# 3.2 View or shallow copy')

c = a.view()
# type
print('type(c) =', type(c))
# c is a
print('c is a:', c is a)
# c.base is a            # c is a view of the data owned by a
print('c.base is a:', c.base is a)
# c.flags.owndata
print('c.flags.owndata:', c.flags.owndata)
# c = c.reshape((2, 6))  # a's shape doesn't change, reassigned c is still a view of a
c = c.reshape((2, 6))
# a.shape
print('a.shape:', a.shape)
# c[0, 4] = 1234         # a's data changes
print('a:\n', a)
# a
print('c:\n', c)

# Slicing an array returns a view of it
s = a[1:2, 1:3]
print('s:\n', s)
print('a:\n', a)
s[:] = -1  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print('s:\n', s)
print('a:\n', a)

