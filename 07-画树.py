import tkinter as Tkinter
import sys, random, math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Point>: (%f, %f)" % (self.x, self.y)


class Branch(object):
    def __init__(self, bottom, top, branches, level=0):
        self.bottom = bottom
        self.top = top
        self.level = level
        self.branches = branches
        self.children = []

    def __str__(self):
        s = "Top: %s, Bottom: %s, Children Count: %d" % (self.top, self.bottom, len(self.children))
        return s

    def nextGen(self, n=-1, rnd=1):
        if n <= 0: n = self.branches
        if rnd == 1:
            n = random.randint(n / 2, n * 2)
            if n <= 0: n = 1
        dx = self.top.x - self.bottom.x
        dy = self.top.y - self.bottom.y
        r = 0.20 + random.random() * 0.2
        if self.top.x == self.bottom.x:
            # 如果是一条竖线
            x = self.top.x
            y = dy * r + self.bottom.y
        elif self.top.y == self.bottom.y:
            # 如果是一条横线
            x = dx * r + self.bottom.x
            y = self.top.y
        else:
            x = dx * r
            y = x * dy / dx
            x += self.bottom.x
            y += self.bottom.y
        oldTop = self.top
        self.top = Point(x, y)
        a = math.pi / (2 * n)
        for i in range(n):
            a2 = -a * (n - 1) / 2 + a * i - math.pi
            a2 *= 0.9 + random.random() * 0.2
            self.children.append(self.mkNewBranch(self.top, oldTop, a2))

    def mkNewBranch(self, bottom, top, a):
        dx1 = top.x - bottom.x
        dy1 = top.y - bottom.y
        r = 0.9 + random.random() * 0.2
        c = math.sqrt(dx1 ** 2 + dy1 ** 2) * r
        if dx1 == 0:
            a2 = math.pi / 2
        else:
            a2 = math.atan(dy1 / dx1)
            if (a2 < 0 and bottom.y > top.y) or (a2 > 0 and bottom.y < top.y):
                a2 += math.pi
        b = a2 - a
        dx2 = c * math.cos(b)
        dy2 = c * math.sin(b)
        newTop = Point(dx2 + bottom.x, dy2 + bottom.y)
        return Branch(bottom, newTop, self.branches, self.level + 1)


class Tree(object):
    def __init__(self, root, canvas, bottom, top, branches=3, depth=3):
        self.root = root
        self.canvas = canvas
        self.bottom = bottom
        self.top = top
        self.branches = branches
        self.depth = depth
        self.new()

    def gen(self, n=1):
        for i in range(n):
            self.getLeaves()
            for node in self.leaves:
                node.nextGen()
        self.show()

    def new(self):
        self.leavesCount = 0
        self.branch = Branch(self.bottom, self.top, self.branches)
        self.gen(self.depth)
        print("leaves count: %d" % self.leavesCount)

    def chgDepth(self, d):
        self.depth += d
        if self.depth < 0: self.depth = 0
        if self.depth > 10: self.depth = 10
        self.new()

    def chgBranch(self, d):
        self.branches += d
        if self.branches < 1: self.branches = 1
        if self.branches > 10: self.branches = 10
        self.new()

    def getLeaves(self):
        self.leaves = []
        self.map(self.findLeaf)

    def findLeaf(self, node):
        if len(node.children) == 0:
            self.leaves.append(node)

    def show(self):
        for i in self.canvas.find_all():
            self.canvas.delete(i)
        self.map(self.drawNode)
        self.canvas.tag_raise("leaf")

    def exit(self, evt):
        sys.exit(0)

    def map(self, func=lambda node: node):
        # 遍历树
        children = [self.branch]
        while len(children) != 0:
            newChildren = []
            for node in children:
                func(node)
                newChildren.extend(node.children)
            children = newChildren

    def drawNode(self, node):
        self.line2(
            #		self.canvas.create_line(
            node.bottom.x,
            node.bottom.y,
            node.top.x,
            node.top.y,
            fill="#100",
            width=1.5 ** (self.depth - node.level),
            tags="branch level_%d" % node.level,
        )

        if len(node.children) == 0:
            # 画叶子
            self.leavesCount += 1
            self.canvas.create_oval(
                node.top.x - 3,
                node.top.y - 3,
                node.top.x + 3,
                node.top.y + 3,
                fill="#090",
                tag="leaf",
            )

        self.canvas.update()

    def line2(self, x0, y0, x1, y1, width=1, fill="#000", minDist=10, tags=""):
        dots = midDots(x0, y0, x1, y1, minDist)
        dots2 = []
        for i in range(len(dots) - 1):
            dots2.extend([dots[i].x,
                          dots[i].y,
                          dots[i + 1].x,
                          dots[i + 1].y])
        self.canvas.create_line(
            dots2,
            fill=fill,
            width=width,
            smooth=True,
            tags=tags,
        )


def midDots(x0, y0, x1, y1, d):
    dots = []
    dx, dy, r = x1 - x0, y1 - y0, 0
    if dx != 0:
        r = float(dy) / dx
    c = math.sqrt(dx ** 2 + dy ** 2)
    n = int(c / d) + 1
    for i in range(n):
        if dx != 0:
            x = dx * i / n
            y = x * r
        else:
            x = dx
            y = dy * i / n
        if i > 0:
            x += d * (0.5 - random.random()) * 0.25
            y += d * (0.5 - random.random()) * 0.25
        x += x0
        y += y0
        dots.append(Point(x, y))
    dots.append(Point(x1, y1))
    return dots


if __name__ == "__main__":
    root = Tkinter.Tk()
    root.title("Tree")
    gw, gh = 800, 600
    canvas = Tkinter.Canvas(root,
                            width=gw,
                            height=gh,
                            )
    canvas.pack()
    tree = Tree(root, canvas, Point(gw / 2, gh - 20), Point(gw / 2, gh * 0.2), branches=2, depth=8)
    root.bind("n", lambda evt: tree.new())
    root.bind("=", lambda evt: tree.chgDepth(1))
    root.bind("+", lambda evt: tree.chgDepth(1))
    root.bind("-", lambda evt: tree.chgDepth(-1))
    root.bind("b", lambda evt: tree.chgBranch(1))
    root.bind("c", lambda evt: tree.chgBranch(-1))
    root.bind("q", tree.exit)
    root.mainloop()
