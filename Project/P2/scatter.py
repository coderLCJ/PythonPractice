import matplotlib.pyplot as plt

x_value = list(range(1, 101))
y_value = [i**2 for i in x_value]

plt.scatter(x_value, y_value, c='red', edgecolors='none', s=5)
 
plt.savefig('test.png')