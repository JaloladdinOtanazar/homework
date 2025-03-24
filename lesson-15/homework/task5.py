import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='b', edgecolor='r', alpha=0.8)
plt.title("Random Data historgam")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

