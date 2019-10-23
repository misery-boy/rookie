"""
    2048游戏核心算法
    1.定义函数，zero_to_end
    [2,0,2,0]>[2,2,0,0]
    [2,0,0,2]>[2,2,0,0]
    [2,4,0,2]>[2,4,2,0]


"""
"""
    核心算法：
    1.定义一个方法，将列表中的0移至列表末尾
    2.定义一个方法，将相邻两个相同的非0元素相加，然后左移至开头
    3.调用1,2函数，以实现将列表向左移动列表的功能，
    4.调用1,2函数，将列表反向以后实现向右移动列表的功能
    5.将矩阵转置以后调用向左移动的函数，再转置，实现向上移动列表的功能
    6.将矩阵转置以后调用向右移动的函数，再转置，实现向下移动列表的功能
"""


list_merge = [4, 4, 4, 4]


def zero_to_end():
    """
    将0元素移至末尾
    :param list_target: 目标列表，list
    :return:
    """

    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    """
    将相邻两位相同的数字相加，然后结尾补0
    :return:
    """

    for i in range(len(list_merge) - 1):
        if list_merge[i] != 0 and list_merge[i] == list_merge[i + 1]:
            list_merge[i] = list_merge[i] * 2
            del list_merge[i + 1]
            list_merge.append(0)


zero_to_end()
merge()
print(list_merge)

map = [
    [2, 2, 0, 0],
    [2, 4, 4, 0],
    [4, 2, 0, 2],
    [2, 4, 2, 0]
]


def transpose_square_matrix(list_square_matrix):
    """
    方针转置
    :param list_square_matrix:目标方阵列表
    :return:
    """
    for r in range(len(list_square_matrix)):
        for c in range(r + 1, len(list_square_matrix[r])):
            list_square_matrix[r][c], list_square_matrix[c][r] = list_square_matrix[c][r], list_square_matrix[r][c]


def move_left():
    """
    将矩阵左移
    :return:
    """
    for r in range(len(map)):
        global list_merge
        list_merge = map[r]
        zero_to_end()
        merge()


def move_right():
    """
    将矩阵右移
    :return:
    """
    for r in range(len(map) - 1, -1, -1):
        global list_merge
        list_merge = map[r][::-1]
        zero_to_end()
        merge()
        map[r] = list_merge[::-1]


def move_up():
    transpose_square_matrix(map)
    move_left()
    transpose_square_matrix(map)


def move_down():
    transpose_square_matrix(map)
    move_right()
    transpose_square_matrix(map)


move_down()

# for i in range(len(map)):
#     for j in range(len(map[i])):
#         print(map[i][j], end=" ")
#     print()

list1 = [1,2,3,4,5]
list1[0] = 10
print(list1)