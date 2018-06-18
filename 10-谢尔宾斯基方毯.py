# 谢尔宾斯基方毯

import pygame

maxlen = 500  # 边界

pygame.init()
screen = pygame.display.set_caption('谢尔宾斯基方毯')
screen = pygame.display.set_mode([maxlen, maxlen])
screen.fill([0, 0, 0])
pygame.display.flip()


def p2(p, r, d):
    # p: 参考左上顶点
    # r: 距离参考点向右偏移距离
    # d: 距离参考点向下偏离距离
    return [p[0] + r, p[1] + d]


def points(p, leni):
    # 返回p,leni对应的四边形四个顶点列表
    return [p, p2(p, leni, 0), p2(p, leni, leni), p2(p, 0, leni)]


def draw(p, leni):
    # p：左上顶点
    # leni：边长
    leni /= 3
    pygame.draw.polygon(screen, [255, 255, 255],
                        points(p2(p, leni, leni), leni))
    if leni > 3:
        draw(p, leni)
        draw(p2(p, leni, 0), leni)
        draw(p2(p, 2 * leni, 0), leni)

        draw(p2(p, 0, leni), leni)
        draw(p2(p, 2 * leni, leni), leni)

        draw(p2(p, 0, 2 * leni), leni)
        draw(p2(p, leni, 2 * leni), leni)
        draw(p2(p, 2 * leni, 2 * leni), leni)
        pygame.display.flip()


draw([0, 0], maxlen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
