import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем сетку значений x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисляем значения функции res для каждой комбинации x и y
Z = 5 * np.sin(((X/2) * np.cosh(0.1*X)) / (np.cos(Y) + 2))

Z_min = Z.min()
print(f"Минимум функции на отрезке от -5 до 5 = {Z_min}")

# Создаем объект для 3D графика
fig = plt.figure(figsize=(300, 300))
ax = fig.add_subplot(111, projection='3d')

# Строим 3D график
ax.plot_surface(X, Y, Z, cmap='viridis')

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображаем график
plt.show()

