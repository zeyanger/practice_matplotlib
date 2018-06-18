import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=3)

# 设置坐标系
plt.title('square_numbers', fontsize=24)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

# 设置刻度大小
plt.tick_params(axis='both', labelsize=24)

plt.show()
