import matplotlib.pyplot as plt
import numpy as np
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
color = np.random.rand(100)
plt.scatter(x, y, c=color, marker = '^', cmap='winter', )
plt.colorbar()
plt.title("Random 100 point")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
