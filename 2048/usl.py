"""
    游戏界面控制器
"""
from bll import GameCoreController


class GameConsoleView:

    def __init__(self):
        self.conctoller = GameCoreController()

    def __start(self):
        """

        :return:
        """
        # 产生随机数X2
        GameCoreController().generate_number()
        GameCoreController().generate_number()
        # 绘制界面

    def __draw_map(self):
        pass

    def __update(self):
        while True:
            dir = input("请输入：")
            if dir == "w":
                self.conctoller.move_up()
                dir = input("请输入：")
            elif dir == "s":
                self.conctoller.move_down()
                dir = input("请输入：")
            elif dir == "a":
                self.conctoller.move_left()
                dir = input("请输入：")
            elif dir == "d":
                self.conctoller.move_right()
            self.conctoller.generate_number()


    def main(self):
        self.__start()
        self.__update()
