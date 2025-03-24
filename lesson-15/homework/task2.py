import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.plot(x, sin_x, 'b,:', label='$sinx$')
plt.plot(x, cos_x, 'ks-.', label='$cosx$')
plt.legend()
plt.show()
