import numpy as np
import pylab as pl
import time
from matplotlib import cm


def iter_point(c):
    z = c
    for i in range(100):
        if abs(z) > 2: return i
        z = z * z + c
    return 100


def draw_mandelbrot(cx, cy, d):
    x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y * 1j
    start = time.clock()
    mandelbrot = np.frompyfunc(iter_point, 1, 1)(c).astype(np.float)
    print("time=", time.clock() - start)
    pl.imshow(mandelbrot, cmap=cm.jet, extent=[x0, x1, y0, y1])
    pl.gca().set_axis_off()


x, y = 0.27322626, 0.595153338

pl.subplot(231)
draw_mandelbrot(-0.5, 0, 1.5)
for i in range(2, 7):
    pl.subplot(230 + i)
    draw_mandelbrot(x, y, 0.2 ** (i - 1))
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()
