import numpy as np
import matplotlib.pyplot as plt
import time
def f(x):
    return x ** 2 + np.sin(x) - 20 * np.cos(x)

def df(x):
    return 2 * x + np.cos(x) + 20 * np.sin(x)

N = 50
xx = 13
lmd = 0.1
x0 = 13

x_plt = np.arange(-2, 20, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()
fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
point = ax.scatter(xx, f(xx), c = 'red')
for j in range(N):
    x0 = x0 - lmd * df(x0)
print(x0)
for i in range(N):
    xx = xx - lmd * df(xx)
    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.2)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='blue')
plt.show()