"""
当大于4的时候，开始处于爆炸状态
什么时候处于爆炸状态：当x超出0到1之间的时候

因为函数的最大值在x=0.5的时候取得，所以最大值不能大于1，也就是r*0.5*0.5不能大于1，所以r不能大于4.

r一旦大于4，就会发散得超级快。
"""


def f(r, x):
    return r * x * (1 - x)


def balance(r):
    x = 0.1
    a = []
    for i in range(1000):
        x = f(r, x)
        print(x)
    for i in range(100):
        x = f(r, x)
        a.append((r, x))
    return a


balance(4)
