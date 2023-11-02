import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Создаем сетку значений x и y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Вычисляем значения функции res для каждой комбинации x и y
Z = 5 * np.sin(((X/2) * np.cosh(0.1*X)) / (np.cos(Y) + 2))

# Создаем объект для 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Строим 3D график
ax.plot_surface(X, Y, Z, cmap='viridis')

# Настройка меток осей
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Значения')

# Отображаем график
plt.show()

