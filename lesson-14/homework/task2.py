import numpy as np
@np.vectorize
def power_number(num, power):
    return num**power
number_array = np.array([2, 3, 4, 5])
power_array = np.array([1, 2, 3, 4])
print(power_number(number_array, power_array))