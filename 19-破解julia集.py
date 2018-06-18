import cv2

in_array = cv2.imread("ailuj/4.png")
print(in_array.shape)

interiorColorMap = []
tmp = 1.0
for i in range(0, 256):
    interiorColorMap.append(tmp)
    tmp *= 7.0 / 8
print(interiorColorMap)

"""
本程序是js翻译成的python
"""


def iterateEquation(Cr, Ci, iterations, Dr, Di):
    Zr = Cr
    Zi = Ci
    Tr = Cr * Cr
    Ti = Ci * Ci
    n = 0
    L = min(Tr, Ti)

    while n < iterations and Tr + Ti <= 100:
        # 当迭代次数足够小且模长小于100
        Zi = 2 * Zr * Zi + Di
        Zr = Tr - Ti + Dr
        Tr = Zr * Zr
        Ti = Zi * Zi
        if Tr < L:
            L = Tr
        if Ti < L:
            L = Ti
        n += 1

    if Tr + Ti > 100:
        v = float(n)
        e = (Tr + Ti) / 100
        if e < 10:
            v -= (e - 1) / 18
        else:
            v -= 0.5 + (e - 10) / 180

        v = v / iterations
        v = 2 * v - v * v
        v = 2 * v - v * v
        return 255 - 255 * v

    v = 0
    s = 128
    while s >= 1:
        if L < interiorColorMap[v + s]:
            v += s
        s //= 2
    return v


def draw(Dr, Di):
    dif = 0
    steps = 256.0
    step = 3.0 / 512

    for sy in range(480):
        if sy % 3 != 0:
            continue
        Ci = (sy + 0.5 - 240) * step
        for sx in range(640):
            if sx % 3 != 0:
                continue
            Cr = (sx + 0.5 - 320) * step
            v = 0.0

            for sr in range(-1, 2):
                for si in range(-1, 2):
                    v += iterateEquation(Cr + sr * step / 4, Ci + si * step / 4, steps, Dr, Di)

            v = v / 9
            C = round(v)
            dif += abs(in_array[sy][sx][1] - C) ** 2
    return dif


dis = 1
dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

dx = -0.175742
dy = 1.085749

min_dif = draw(dx, dy)
print(dx, dy, min_dif)

get_dict = {}
"""
从一个点开始尝试往四个方向搜索
"""
while dis > 0.00000005:
    while 1:
        t_min_dif = min_dif
        for d in range(0, 4):
            tdx = dx + dis * dirs[d][0]
            tdy = dy + dis * dirs[d][1]
            if (tdx, tdy) in get_dict:
                continue
            new_dif = draw(tdx, tdy)
            get_dict[(tdx, tdy)] = new_dif
            print(tdx, tdy, new_dif)
            if new_dif < min_dif:
                min_dif = new_dif
                dx, dy = tdx, tdy
                continue
        if min_dif == t_min_dif:
            dis /= 2
            break

print(dx, dy, min_dif)
