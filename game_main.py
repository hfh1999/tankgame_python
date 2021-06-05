from scene_manager import SceneManager


class GameMain:
    def __init__(self):
        self.scene_array = []
        self.manager = SceneManager(self.scene_array)  # 负责调度场景

    def run(self):
        print("start game here")
        self.manager.run()
