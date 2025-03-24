import matplotlib.pyplot as plt
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['r', 'b', 'skyblue', 'g', 'grey']
plt.bar(categories, values, color=colors, edgecolor='black')
plt.title('The Sales Data For 5 Products')
plt.xlabel('Categories')
plt.ylabel("Values")
plt.show()