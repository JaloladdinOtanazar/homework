import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10,9))  
x = np.linspace(-5, 5, 100)
positive_x = np.linspace(0, 3, 100)
#top left
axes[0,0].plot(x, x**3, 'r.--', label='$ f(x) = x^3 $')
axes[0,0].set_xlabel('X')
axes[0,0].set_ylabel('Y')
axes[0,0].legend()
#top right
axes[0,1].plot(x, np.sin(x), 'g.--', label='$ f(x) = sinx $')
axes[0,1].set_xlabel('X')
axes[0,1].set_ylabel('Y')
axes[0,1].legend()
#bottom left
axes[1,0].plot(x, np.exp(positive_x), 'b.-.', label='$ f(x) = e^x $')
axes[1,0].set_xlabel('X')
axes[1,0].set_ylabel('Y')
axes[1,0].legend()
#bottom right
axes[1,1].plot(x, np.log(positive_x + 1), 'k.-.', label='$ f(x) = e^x $')
axes[1,1].set_xlabel('X')
axes[1,1].set_ylabel('Y')
axes[1,1].legend()
plt.show()


