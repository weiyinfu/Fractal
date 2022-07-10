import numpy as np
import pylab as plt
from tqdm import tqdm

"""
不仅仅是二次函数 f_r(x)=r*x*(1-x)，任何一个类似半圆的函数都会产生同样的分形。  
因为sin(x)在x=pi/2的时候取得最大值1
"""


def f(r, x):
    return r * np.sin(x)


def balance(r):
    x = 0.1
    a = []
    for i in range(1000):
        x = f(r, x)
    for i in range(100):
        x = f(r, x)
        a.append((r, x))
    return a


def main():
    rs = np.linspace(0.1, 15, 1000)
    ps = []
    for r in tqdm(rs):
        ps.extend(balance(r))
    ps = np.array(ps)
    # print(max(ps[:, 0]), min(ps[:, 0]))
    plt.scatter(ps[:, 0], ps[:, 1], s=0.5)
    # plt.ylim(0, 3)
    plt.show()


main()
