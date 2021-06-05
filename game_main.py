from scene_manager import SceneManager
import pygame as pg


class GameMain:
    def __init__(self):
        self.scene_array = []
        pg.display.init()
        self.screen = pg.display.set_mode((500, 500))  # 这里是用于显示的屏幕
        self.manager = SceneManager(self.scene_array, self.screen)  # 负责调度场景

    def run(self):
        print("start game here")
        self.manager.run()
