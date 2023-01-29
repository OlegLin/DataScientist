import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

x_plt = np.arange(-10, 10, 0.1)
y_plt = [f(x) for x in x_plt]
ax.scatter(x_plt, y_plt, c='red')
plt.show()