# 方块分形

import pygame

maxlen = 500  # 边界

pygame.init()
screen = pygame.display.set_caption('方块分形')
screen = pygame.display.set_mode([maxlen, maxlen])
screen.fill([255, 255, 255])
pygame.display.flip()


def draw(st, leni):
    # st: 左上角点位置[left,top]
    # leni: 当前方块边长
    if leni > 3:
        leni /= 3
        draw(st, leni)  # 左上
        draw([st[0] + leni * 2, st[1]], leni)  # 右上
        draw([st[0] + leni, st[1] + leni], leni)  # 中间
        draw([st[0], st[1] + leni * 2], leni)  # 左下
        draw([st[0] + leni * 2, st[1] + leni * 2], leni)  # 右下
        pygame.display.flip()
    else:
        pygame.draw.rect(screen, [0, 0, 0], [st[0], st[1], leni, leni])


draw([0, 0], maxlen)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
