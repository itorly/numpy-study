import numpy as np
from numpy import pi

# In NumPy, you can compute the sine of a value and represent the result using π (pi) by leveraging the numpy.sin function and the numpy.pi constant. However, the result of numpy.sin is a numerical value, and it doesn't directly represent the result in terms of π. Instead, you can express the input in terms of π and then compute the sine.
# Here's an example of how you can compute the sine of a value expressed in terms of π:
# Define the angle in terms of pi
angle_in_pi = np.pi / 4  # 45 degrees in radians

# Compute the sine of the angle
sine_value = np.sin(angle_in_pi)

# Print the result
print(f'sin({angle_in_pi}π) = {sine_value}')

# For known angles, you can also print the exact value
if np.isclose(angle_in_pi, np.pi / 4):
    print(f'sin(π/4) = √2/2')

# The angle is expressed as a fraction of π, and the sine value is printed.
# Create an array of angles in terms of pi
angles_in_pi = np.array([0, pi / 6, pi / 4, pi / 3, pi / 2, 2 * pi / 3, 3 * pi / 4, 5 * pi / 6, pi])

# Compute the sine of each angle
sine_values = np.sin(angles_in_pi)


# Function to represent sine values in terms of pi
def represent_in_terms_of_pi(value):
    # Known sine values and their corresponding fractions of pi
    known_values = {
        0: '0',
        0.5: '1/2',
        np.sqrt(2) / 2: '√2/2',
        np.sqrt(3) / 2: '√3/2',
        1: '1'
    }

    # Find the closest known value
    for known_value, representation in known_values.items():
        if np.isclose(value, known_value):
            return representation
    return str(value)


# Represent each sine value in terms of pi
sine_values_in_pi = [represent_in_terms_of_pi(value) for value in sine_values]

# Print the results
for angle, sine_value in zip(angles_in_pi, sine_values_in_pi):
    print(f'sin({angle / pi}π) = {sine_value}')