import matplotlib.pyplot as plot
import numpy as np

N = 256  # 最大迭代次数
M = 2  # 迭代区域的界值
x_limit = 3.0  # 绘制图的横轴大小
y_limit = 3.0  # 绘制图的纵轴大小
step = 0.005  # 绘制点的步长


def iterate(z, N, M):
    z = z * z + c
    for i in range(N):
        if abs(z) > M:  # 溢出了，不收敛
            return i
        z = z * z + c
    return N


c = 0.4 + 0.3j
i = np.arange(-x_limit / 2.0, x_limit / 2.0, step)
j = np.arange(y_limit / 2.0, -y_limit / 2.0, -step)
I, J = np.meshgrid(i, j)
ufunc = np.frompyfunc(iterate, 3, 1)
Z = ufunc(I + 1j * J, N, M).astype(np.float)
plot.imshow(Z, extent=(-x_limit / 2.0, x_limit / 2.0, -y_limit / 2, y_limit / 2.0), cmap="hsv")
cb = plot.colorbar(orientation='vertical', shrink=1)
cb.set_label('iteration counts')
plot.show()
