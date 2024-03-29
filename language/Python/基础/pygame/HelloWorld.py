import pygame,sys

pygame.init()


screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("你好，世界")

# 列出显卡支持的显示模式
print(pygame.display.list_modes())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


