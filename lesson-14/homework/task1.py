import numpy as np
@np.vectorize
def convert(temp):
    return (temp-32)*(5/9)

arr = np.array([32, 68, 100, 212, 77])
print(convert(arr))