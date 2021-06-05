from basic_scene import BasicScene


class SceneManager:
    # 初始化时记得要传入一个空数组，用以存储加载的场景
    def __init__(self, scenes, screen):
        self.__scene_ptr = None  # 表示目前是哪个场景，初始化时啥也没有
        self.__scene_array_ptr = scenes
        self.__screen_ptr = screen
        print("init SceneManager")

        self.__scene_array_ptr.append(1)

    def run(self):  # 这里运行管理器
        print("SceneManager running")

        """
            这里写一个状态机
            开始 -> 场景1 -> 场景2 -> ... -> 结束 
        """
        self.__scene_ptr = BasicScene(self.__screen_ptr)  # 开始
        while True:
            self.__scene_ptr.deal()
