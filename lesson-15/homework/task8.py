import matplotlib.pyplot as plt
import numpy as np
category_a = [1,3,5,7]
category_b = [2,4,6,5]
category_c = [4,2,7,5]

time_period = ['T1', 'T2', 'T3', 'T4']
plt.bar(time_period, category_a, label='Category A', color='b')
plt.bar(time_period, category_b, label='Category B', color='skyblue')
plt.bar(time_period, category_c, label='Category C', color='grey')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.legend()
plt.show()
