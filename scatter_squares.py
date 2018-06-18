# !/usr/bin/Python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.Reds)

# 设置图标标题并给坐标轴加标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
