# 谢尔宾斯基三角垫

import pygame

maxlen = 500  # 边界

pygame.init()
screen = pygame.display.set_caption('谢尔宾斯基三角垫')
screen = pygame.display.set_mode([maxlen, maxlen])
screen.fill([255, 255, 255])
pygame.display.flip()


def mid(a, b):
    # 求出a, b点的中点坐标
    return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]


def draw(one, two, tri):
    # 参数代表三个顶点,上、左、右排序
    if one[0] - two[0] > 2:  # 可分
        draw(one, mid(one, two), mid(one, tri))  # 画上面的三角
        draw(mid(one, two), two, mid(two, tri))  # 画左边三角
        draw(mid(one, tri), mid(two, tri), tri)  # 画右边的三角
        pygame.display.flip()
    else:  # 达到最小结构
        pygame.draw.polygon(screen, [0, 0, 0], [one, two, tri])


draw([maxlen / 2, 0], [0, maxlen], [maxlen, maxlen])
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
