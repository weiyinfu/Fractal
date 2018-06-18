"""
在一单位长度的线段上对其三等分，将中间段直线换成一个去掉底边的等边三角形，
再在每条直线上重复以上操作，如此进行下去直到无穷，就得到分形曲线Koch曲线。
"""

import turtle
import tkinter


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


t = turtle.Pen()
t.pensize(3)
t.pencolor("red")
R = t.screen.canvwidth / 2
t.penup()
t.goto(-R, 0)
t.pendown()
t.speed(100000)
for i in range(6):  # 六边形科赫雪花
    angle = i * (-60) + 60
    t.setheading(angle)
    koch(t, 3, R)
tkinter.mainloop()
