import random

import numpy as np
from matplotlib import pyplot as plt

a = np.array([[0.195, -0.488, 0.344, 0.433, 0.4431, 0.2452, 0.25],
              [0.462, 0.414, -0.252, 0.361, 0.2511, 0.5692, 0.25],
              [-0.058, -0.07, 0.453, -0.111, 0.5976, 0.0969, 0.25],
              [-0.035, 0.07, -0.469, -0.022, 0.4884, 0.5069, 0.2],
              [-0.637, 0, 0, 0.501, 0.8562, 0.2513, 0.05]])
x0 = 1
y0 = 1
for i in range(10000):
    r = random.random()
    if r <= 0.25:
        ind = 0
    elif r <= 0.5:
        ind = 1
    elif r <= 0.75:
        ind = 2
    elif r <= 0.95:
        ind = 3
    else:
        ind = 4
    x1 = a[ind, 0] * x0 + a[ind, 1] * y0 + a[ind, 4]
    y1 = a[ind, 2] * x0 + a[ind, 3] * y0 + a[ind, 5]
    x0, y0 = x1, y1
    plt.scatter([x1], [y1])
plt.show()
