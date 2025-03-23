import numpy as np
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])
b = np.array([7, 4, 5])
x = np.linalg.solve(A, b)
print(f"x: {round(x[0], 3)}, y: {round(x[1], 3)}, z: {round(x[2], 3)}")