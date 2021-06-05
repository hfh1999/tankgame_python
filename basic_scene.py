import pygame as pg

"""
基本场景用于游戏基本资源的加载
"""


class BasicScene:
    def __init__(self, screen: pg.Surface):  # 还需要传入一个参数表示将这个场景显示在哪里
        # 进行pygame的初始化
        print("BasicScene: 初始化一些这个场景需要的pygame事项")
        print(screen.get_size())  # 显示场景大小
        screen.fill((250, 250, 250))
        # pg.init()
        # screen = pg.display.set_mode((500, 500))  # 创建屏幕
        # pg.display.set_caption("Hello tank game")
        # pg.mouse.set_visible(0)

        # background = pg.Surface(screen.get_size())
        # background = background.convert()
        # background.fill((250, 0, 250))

        # screen.blit(background, (0, 0))
        # pg.display.flip()

        # while True:
        #    pass

    def deal(self):
        pg.display.flip()
        pass
