# 康托集
import pygame

"""
选取一个欧氏长度的直线段，将该线段三等分，去掉中间一段，剩下两段。
将剩下的两段分别再三等分，各去掉中间一段，剩下四段。
将这样的操作继续下去，直到无穷，则可得到一个离散的点集。
点数趋于无穷多，而欧氏长度趋于零。经无限操作，达到极限时所得到的离散点集称之为Cantor集。
"""

pygame.init()
screen = pygame.display.set_caption('康托集')
screen = pygame.display.set_mode([1000, 250])
screen.fill([255, 255, 255])
pygame.display.flip()

len0 = 1000  # 初始线条长度
leni = len0  # 当前最小线条长度
line = 0  # 当前行数

while leni > 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    n = 2 ** line  # 集合元素份数
    tep = [0, ]  # 元素第一个端点位置
    while len(tep) < n:
        nt = (tep[-1] + leni) * 2  # 接下来首个元素位置
        tepp = []  # 接下来元素位置
        for j in tep:
            tepp.append(nt + j)
        tep.extend(tepp)
    for k in tep:
        pygame.draw.line(screen, [0, 0, 0], [
            k, 30 * line + 5], [k + leni, 30 * line + 5], 10)
    pygame.display.flip()
    line += 1
    leni = leni / 3

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
