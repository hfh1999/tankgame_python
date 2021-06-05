import pygame as pg
from pygame.locals import *  # 引入常用的变量


class BasicScene:
    def __init__(self):
        # 进行pygame的初始化
        print("BasicScene: init pygame")
        pg.init()
        screen = pg.display.set_mode((500, 500))  # 实验全屏幕
        pg.display.set_caption("Hello tank game")
        pg.mouse.set_visible(0)

        background = pg.Surface(screen.get_size())
        background = background.convert()
        # background.fill((250, 0, 250))

        screen.blit(background, (0, 0))
        pg.display.flip()

        while True:
            pass
