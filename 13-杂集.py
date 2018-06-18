from math import sin, cos, pi
import matplotlib.pyplot as pl
from matplotlib import collections


class L_System:
    def __init__(self, rule):
        # 根据规则初始化self的info和rule
        info = rule['S']
        for i in range(rule['iter']):
            next_info = []
            for c in info:
                if c in rule:
                    next_info.append(rule[c])
                else:
                    next_info.append(c)
            info = ''.join(next_info)
        self.rule = rule
        self.info = info

    def get_lines(self):
        d = self.rule["direct"]  # 方向
        a = self.rule["angle"]  # 角度
        p = (0.0, 0.0)  # 初始位置
        l = 1.0  # 步长
        lines = []
        stack = []
        for c in self.info:
            if c in "Ff":  # 向前走
                r = d * pi / 180
                t = p[0] + l * cos(r), p[1] + l * sin(r)
                lines.append(((p[0], p[1]), (t[0], t[1])))
                p = t
            elif c == "+":
                d += a  # 遇到加号，转向角度增大
            elif c == "-":
                d -= a  # 遇到减号，转向角度减小
            elif c == "[":  # 遇到左中括号，入栈
                stack.append((p, d))
            elif c == "]":  # 遇到右中括号
                p, d = stack[-1]
                del stack[-1]
        return lines


rules = [
    # 用有限状态自动机来描述分形
    {"F": "F+F--F+F",  # 科赫分形
     "S": "F",
     "direct": 180,
     "angle": 60,
     "iter": 5,
     "title": "Koch",
     }, {  # 龙
        "X": "X+YF+",
        "Y": "-FX-Y",
        "S": "FX",
        "direct": 0,
        "angle": 90,
        "iter": 13,
        "title": "Dragon",
    }, {  # 三角形
        "f": "F-f-F", "F": "f+F+f", "S": "f",
        "direct": 0,
        "angle": 60,
        "iter": 7,
        "title": "Triangle",
    }, {  # 平面图
        "X": "F-[[X]+X]+F[+FX]-X", "F": "FF", "S": "X",
        "direct": -45,
        "angle": 25,
        "iter": 6,
        "title": "Plant"
    }, {  # 希尔伯特
        "S": "X",
        "X": "-YF+XFX+FY-",
        "Y": "+XF-YFY-FX+",
        "direct": 0,
        "angle": 90,
        "iter": 6,
        "title": "Hilbert"
    }, {  # 谢尔宾斯基
        "S": "L--F--L--F",
        "L": "+R-F-R+",
        "R": "-L+F+L-",
        "direct": 0,
        "angle": 45,
        "iter": 10,
        "title": "Sierpinski",
    }
]


def draw(ax, rule, iter=None):
    if iter is not None:
        rule['iter'] = iter
    lines = L_System(rule).get_lines()
    linecollections = collections.LineCollection(lines)
    ax.add_collection(linecollections, autolim=True)
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    ax.invert_yaxis()


fig = pl.figure(figsize=(7, 4.5))
fig.patch.set_facecolor("papayawhip")

for i in range(6):
    print(i)
    ax = fig.add_subplot(231 + i)
    draw(ax, rules[i])
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
pl.show()
