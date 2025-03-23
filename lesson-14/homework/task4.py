import numpy as np
A = np.array([
    [10, -2, 3],
    [-2, 8, -10],
    [3, -1, 6]
])
b = np.array([12, -5, 15])
x = np.linalg.solve(A, b)
print(f"I1: {round(x[0], 3)}, I2: {round(x[1], 3)}, I3: {round(x[2], 3)}")