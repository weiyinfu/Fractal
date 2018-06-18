# 康托尘埃

import pygame

pygame.init()
screen = pygame.display.set_caption('康托尘埃')
screen = pygame.display.set_mode([487, 487])
screen.fill([255, 255, 255])
pygame.display.flip()

cantor = [1, ]  # 起点集，最小像素为1

while (cantor[-1] + 1) * 3 < 1000:
    st = (cantor[-1] + 1) * 2  # 下一迭代起点
    tep = []
    for i in cantor:
        tep.append(st + i)  # 重复上一子集
    cantor.extend(tep)
# print(cantor[-1]) # 输出最大像素起点
for i in cantor:
    for j in cantor:
        screen.set_at([i, j], [0, 0, 0])
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()