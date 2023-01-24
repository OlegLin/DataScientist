import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
a = []

# for i in range(1, 11):
#   a.append(i)
#
# print(np.linspace(1, 10, 4, dtype=float))
# print(np.arange(1, 10, 3))

A = np.array([[1, 2], [3, 4]], dtype=float)
print(A)
print(np.linalg.inv(A))
print(A@np.linalg.inv(A))
# def f(x):
#   return x ** 2 + math.sin(x) - math.log(1+x)
#
# xs = [-1, 0, 1]
# ys = [1, 0, 1]
#
# plt.plot(xs, ys)