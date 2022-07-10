"""
分形的速度有多快？
分叉的速度越来越快，是指数级的分叉。

由于费根鲍姆的常数大于1，也就是说倍周期分叉的“距离”之比是一个等比数列，而这个等比数列虽然有无限多项，但总和是有限的。在参数b小于3.57时，这种以2为周期开始的倍周期分叉已经结束了。而当参数b大于3.57时，开始出现周期3开始的倍周期分叉——而根据李天岩与约克的定理：“周期3的出现预示着混沌的出现”，这意味着在抛物线映射中，也是可以出现混沌的。

三体问题，世间万物到了三就变得错综复杂。
一元n次方程求解问题，到了5就没有了解析式。
"""
import numpy as np


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


def point_count(r):
    a = np.array(balance(r))[:, 1]
    a.sort()
    b = []
    for i in a:
        if b and i - b[-1] < 1e-2:
            continue
        else:
            b.append(i)
    return len(b)


def main():
    rs = np.linspace(0.1, 4, 1000)
    a = [point_count(r) for r in rs]
    print(a)
    # 第一个分叉点
    ind = a.index(2)
    print(rs[ind])
    # 第二个分叉点
    ind = a.index(4)
    print(rs[ind])
    ind = a.index(7)
    print(rs[ind])


def see():
    a = 3.0006006006006007
    b = 3.4534534534534536
    c = 3.547147147147147
    print((b - a) / (c - b))  # 4.833333333333337
    """
    出现倍周期分叉的b的那些数值，距离之比接近一个常数，这个常数大概等于4.6692
    """


# main()
see()
