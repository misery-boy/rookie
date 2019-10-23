"""
    可迭代对象常用工具
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    # 静态方法：函数(不需要操作实例/类数据) --> 方法
    @staticmethod  # 为了不隐式(自动)传参(self/cls)
    def find_all(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件搜索元素.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:生成器对象,存储满足条件的结果.
        """
        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable_target, func_condition):
        """

            在可迭代对象中，根据指定条件搜索单个元素.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:生成器对象,存储满足条件的结果.
        """
        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count_all(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件计数
        :param iterable_target: 需要计数的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 计数值,int
        """
        count = 0
        for item in iterable_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def sum_value(iterable_target, func_condition):
        """
            在可迭代对象中，根据规则计算总和
        :param iterable_target: 需要计算的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 总数值,int
        """
        sum_value = 0
        for item in iterable_target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def judge(iterable_target, func_condition):
        """
            在可迭代对象中，根据规则判断是否存在特定元素
        :param iterable_target: 需要计算的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 是否，bool
        """
        for item in iterable_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_max(iterable_target, func_condition):
        """
            在可迭代对象中，获取最大值
        :param iterable_target: 需要计算的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 最大项
        """
        max_value = iterable_target[0]
        for i in range(1, len(iterable_target)):
            if func_condition(iterable_target[i]) > func_condition(max_value):
                max_value = iterable_target[i]
        return max_value

    @staticmethod
    def get_min(iterable_target, func_condition):
        """
            在可迭代对象中，获取最小值
        :param iterable_target: 需要计算的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 最小项
        """
        min_value = iterable_target[0]
        for i in range(1, len(iterable_target)):
            if func_condition(iterable_target[i]) > func_condition(min_value):
                min_value = iterable_target[i]
        return min_value

    @staticmethod
    def select(iterable_target, func_condition):
        """
            在可迭代对象中，获取元素
        :param iterable_target: 需要计算的可迭代对象
        :param func_condition: 需要判断的条件
        :return: 生成器对象,存储满足条件的结果
        """
        for item in iterable_target:
            yield func_condition(item)

    @staticmethod
    def order_by(iterable_target, func_condition):
        """
            将可迭代元素按照规则进行升序排列
        :param iterable_target: 可迭代对象
        :param func_condition: 判断条件
        :return: 无
        """
        for i in range(0, len(iterable_target) - 1):
            for j in range(1, len(iterable_target)):
                if func_condition(iterable_target[i]) > func_condition(iterable_target[j]):
                    iterable_target[i], iterable_target[j] = iterable_target[j], iterable_target[i]

    @staticmethod
    def order_by_descending(iterable_target, func_condition):
        """
            将可迭代元素按照规则进行降序排列
        :param iterable_target: 可迭代对象
        :param func_condition: 判断条件
        :return: 无
        """
        for i in range(0, len(iterable_target) - 1):
            for j in range(1, len(iterable_target)):
                if func_condition(iterable_target[i]) < func_condition(iterable_target[j]):
                    iterable_target[i], iterable_target[j] = iterable_target[j], iterable_target[i]

    @staticmethod
    def delete_all(iterable_target, func_condition):
        """
            将可迭代元素按照规则进行删除
        :param iterable_target: 可迭代对象
        :param func_condition: 判断条件
        :return: 无
        """
        for i in range(len(iterable_target), -1, -1):
            if func_condition(iterable_target[i]):
                del iterable_target[i]

    @staticmethod
    def delete_single(iterable_target, func_condition):
        """
            将可迭代元素按照规则进行删除（只删第一个）
        :param iterable_target: 可迭代对象
        :param func_condition: 判断条件
        :return: 无
        """
        for i in range(len(iterable_target)-1, -1, -1):
            if func_condition(iterable_target[i]):
                del iterable_target[i]
                return
