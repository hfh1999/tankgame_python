from basic_scene import BasicScene


class SceneManager:
    # 初始化时记得要传入一个空数组，用以存储加载的场景
    def __init__(self, scenes):
        self.__scene_ptr = None  # 表示目前是哪个场景，初始化时啥也没有
        print("init SceneManager")

    def run(self):  # 这里运行管理器
        print("SceneManager running")

        """
            这里写一个状态机
            开始 -> 场景1 -> 场景2 -> ... -> 结束 
        """
        self.__scene_ptr = BasicScene()  # 开始
