# !/usr/bin/Python
# -*- coding: utf-8 -*-


from random import choice


class RandomWalk:
    """初始化随机漫步数据的类"""

    def __init__(self, num_points=5000):
        # 初始化属性
        self.num_points = num_points

        # 所有随机漫步都始于（0， 0）
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步的所有点"""

        # 不断漫步知道达到指定的长度
        while len(self.x_value) < self.num_points:
            # 决定前进方向及距离
            x_direction = choice([-1, 1])
            x_distance = choice([range(6)])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([range(6)])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
