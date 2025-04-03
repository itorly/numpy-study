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

# 5.3 Histograms
print('\n# 5.3 Histograms')

import numpy as np
rg = np.random.default_rng(1)
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=True)       # matplotlib version (plot)
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
# plt.show()
plt.savefig('histogram.png')