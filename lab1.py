import math
import random

def f(x:float, y:float) -> float:
    res = 5*math.sin(((x/2)*math.cosh(0.1*x))/(math.cos(y)+2))
    return res

def temp():
    t = 100
    while t >= 0.5:
        yield t
        t = t/2

for t in temp():
    print(t)

# Генерация случайного числа с плавающей запятой в диапазоне от -5 до 5
random_float = random.uniform(-5, 5)
print(random_float)

import matplotlib.pyplot as plt

# Ваши значения
values = [100, 50.0, 25.0, 12.5, 6.25, 3.125, 1.5625, 0.78125]

# Создаем список значений на оси x от 0 до 150
x_values = [i * 150 / 8 for i in range(9)]

# Строим график
plt.plot(x_values, values, marker='o', linestyle='-', color='b')
plt.xlabel('Ось X')
plt.ylabel('Значения')
plt.title('График значений')

# Отображаем график
plt.show()
