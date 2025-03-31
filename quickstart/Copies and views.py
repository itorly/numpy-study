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