import numpy as np
import pylab as plt
from tqdm import tqdm

"""
f_r(x)=r*x*(1-x)
r是一个超参数，这个函数迭代若干次之后，会是什么样子？设迭代若干次之后的状态为balance(r)。    
当r比较小的时候，这个函数总是会趋向于一个值。  
当r再大一点的时候，最终的状态在两个值之间震荡。  
当r再大一点的时候，最终的状态在4个值之间震荡。  
当r再大一点的时候，最终的状态在8个值之间震荡。  
"""


def f(r, x):
    return r * x * (1 - x)


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
    rs = np.linspace(0.1, 4, 1000)
    ps = []
    for r in tqdm(rs):
        ps.extend(balance(r))
    ps = np.array(ps)
    # print(max(ps[:, 0]), min(ps[:, 0]))
    plt.scatter(ps[:, 0], ps[:, 1], s=0.5)
    # plt.ylim(0, 3)
    plt.show()


main()
