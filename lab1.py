import random
import numpy as np

def f(x:float, y:float) -> float:
    """
    Функция энергии, целевая функция для минимизации
    """
    res: float = 5 * np.sin(((x/2) * np.cosh(0.1*x)) / (np.cos(y) + 2))
    return res

def temp():
    """
    Функция генерации значений температуры
    """
    t: float = 100
    while t >= 0.5:
        yield t
        t = t/2

def temp_new():
    """
    Функция генерации значений температуры
    модифицированная
    """
    t: float = 100
    while t >= 0.01:
        yield t
        t = t/1.2

def translate(probability: float) -> bool:
    """
    Функция перехода: генерирует случайное значение от 0 до 1
    выполняет переход если сгенерированное значение
    меньше ли равно вероятности перехода
    probability - вероятность перехода
    """
    probe_value = random.uniform(0,1)
    if probe_value <= probability:
        return True
    return False

x_y_range: float = 5
# Генерация случайного числа с плавающей запятой в диапазоне от -5 до 5
# начальное значение
x_current: float = random.uniform(-x_y_range, x_y_range)
y_current: float = random.uniform(-x_y_range, x_y_range)

# задаю начальное значение для энергии
energy_state: float = f(x_current, y_current)

# промежуток, в котором будут генерироваться новые значения
new_range: float = 2.0

print(f"Начальная энергия {energy_state:.6f}")
print(f"X: {x_current:.6f}; Y: {y_current:.6f}")

for current_temp in temp_new():
    # случайное изменение текущего решения
    new_x_current: float = x_current + random.uniform(-new_range, new_range)
    new_y_current: float = y_current + random.uniform(-new_range, new_range)

    # ограничение новых значений нашим промежутком поиска
    new_x_current = np.clip(new_x_current, -x_y_range, x_y_range)
    new_y_current = np.clip(new_y_current, -x_y_range, x_y_range)

    # вычисляю значение энергии в новой точке
    new_energy_state: float = f(new_x_current, new_y_current)

    # рассчитываю вероятность перехода в новое состояние
    # exp^(-(new_energy - energy)/Ti)
    probability: float = np.clip(np.exp(-(new_energy_state-energy_state)/current_temp), 0, 1)

    print(f"Температура: {current_temp:3.3f};\t\
текущая энергия {energy_state:3.7f};\t\
новая энергия {new_energy_state:3.7f};\t\
вероятность перехода: {probability:3.2f}")

    # выполняю переход, если случайное значение попадает
    # в промежуток вероятности перехода
    if translate(probability):
        x_current = new_x_current
        y_current = new_y_current
        energy_state = new_energy_state

print(f"Вычисленное значение: {energy_state:.6f}")
print(f"X: {x_current:.6f}; Y: {y_current:.6f}")
