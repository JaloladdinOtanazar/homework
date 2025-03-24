import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10000)
y = (x-2)**2
plt.plot(x, y, label='$ f(x) = x^2 - 4x + 4 $')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y', rotation=100)
plt.legend()
plt.show()

