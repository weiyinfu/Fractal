import numpy as np
import matplotlib.pyplot as pl
import time

eq = np.array([[[0, 0, 0], [0, 0.16, 0]],
               [[0.2, -0.26, 0], [0.23, 0.22, 1.6]],
               [[-0.15, 0.28, 0], [0.26, 0.24, 0.44]],
               [[0.85, 0.04, 0], [-0.04, 0.85, 1.6]]
               ])
p = [0.01, 0.07, 0.07, 0.85]


def ifs(p, eq, init, n):
    pos = np.ones(3, dtype=np.float)
    pos[:2] = init
    p = np.add.accumulate(p)
    rands = np.random.rand(n)
    select = np.ones(n, dtype=np.int) * (n - 1)
    for i, x in enumerate(p[::-1]):
        select[rands < x] = len(p) - 1 - i
    result = np.zeros((n, 2), dtype=np.float)
    c = np.zeros(n, dtype=np.float)

    for i in range(n):
        eqidx = select[i]
        tmp = np.dot(eq[eqidx], pos)
        pos[:2] = tmp
        result[i] = tmp
        c[i] = eqidx
    return result[:, 0], result[:, 1], c


start = time.clock()
x, y, c = ifs(p, eq, [0, 0], 100000)
print(time.clock() - start)
pl.figure(figsize=(6, 6))
pl.subplot(121)
pl.scatter(x, y, s=1, c='g', marker='s', linewidths=0)
pl.axis("equal")
pl.axis("off")
pl.subplot(122)
pl.scatter(x, y, s=1, c=c, marker="s", linewidths=0)

pl.axis("equal")
pl.axis("off")

pl.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
pl.gcf().patch.set_facecolor("#D3D3D3")
pl.show()
