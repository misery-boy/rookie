"""
    伪随机：先将为0的位置放入容器，然后再随机挑选一个位置生成
    随机生成2（90%)4（10%）

"""
import random


class GameCoreController:

    def __init__(self):
        self.__list = []
        self.__map = [[2, 4, 2, 4],
                      [4, 2, 8, 2],
                      [8, 4, 2, 8],
                      [4, 2, 4, 4]]
        self.__zero_location = []

    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        """
        将0元素移至末尾
        :return:
        """

        for i in range(len(self.__list) - 1, -1, -1):
            if self.__list[i] == 0:
                del self.__list[i]
                self.__list.append(0)

    def merge(self):
        """
        将相邻两位相同的数字相加，然后结尾补0
        :return:
        """

        for i in range(len(self.__list) - 1):
            if self.__list[i] != 0 and self.__list[i] == self.__list[i + 1]:
                self.__list[i] = self.__list[i] * 2
                del self.__list[i + 1]
                self.__list.append(0)

    def transpose_square_matrix(self):
        """
        方阵转置
        :return:
        """
        for r in range(len(self.__list)):
            for c in range(r + 1, len(self.__list[r])):
                self.__list[r][c], self.__list[c][r] = self.__list[c][r], self.__list[r][c]

    def move_left(self):
        """
        将矩阵左移
        :return:
        """
        for r in range(len(self.__map)):
            self.__list = self.__map[r]
            self.zero_to_end()
            self.merge()

    def move_right(self):
        """
        将矩阵右移
        :return:
        """
        for r in range(len(self.__map) - 1, -1, -1):
            self.__list = self.__map[r][::-1]
            self.zero_to_end()
            self.merge()
            self.__map[r] = self.__list[::-1]

    def move_up(self):
        """
        将矩阵上移（先将矩阵转置，然后向左移动，再转置，完成上移）
        :return:
        """
        self.transpose_square_matrix()
        self.move_left()
        self.transpose_square_matrix()

    def move_down(self):
        """
        将矩阵下移（先将矩阵转置，然后向右移动，再转置，完成下移）
                 and self
        :return:
        """
        self.transpose_square_matrix()
        self.move_right()
        self.transpose_square_matrix()

    def __get_zero_location(self):
        self.__zero_location.clear()
        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                if self.__map[i][j] == 0:
                    self.__zero_location.append((i, j))

    def __choose_location(self):
        # self.__locate = random.randint(0, len(self.__location)-1)
        locate = random.choice(self.__zero_location)
        return locate

    def generate_number(self):
        self.__get_zero_location()
        locate = self.__choose_location()
        self.__map[locate[0]][locate[1]] = 2 if random.randint(1, 10) != 4 else 4
        self.__zero_location.remove(locate)
        # random_num = random.randint(1, 10)
        # if random_num != 4:
        #     self.__map[self.__location[self.__locate][0]][self.__location[self.__locate][1]] = 2 if
        # else:
        #     self.__map[self.__location[self.__locate][0]][self.__location[self.__locate][1]] = 4

    def juedge_end_game(self):
        """
            判断游戏结束条件：1.没有空位置
                        2.水平与垂直方向均没有可合并的数字
        :return:
        """
        if len(self.__zero_location) != 0:
            return False
        self.__get_zero_location()
        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])-1):
                if self.__map[i][j] == self.__map[i][j + 1] or self.__map[j][i] == self.__map[j][i-1]:  # 牛逼
                    return False
        return True


if __name__ == "__main__":
    g1 = GameCoreController()
    # g1.move_left()
    # for item in g1.map:
    #     print(item)
    #
    # g1.generate_number()
    # for item in g1.map:
    #     print(item)

    print(g1.juedge_end_game())
