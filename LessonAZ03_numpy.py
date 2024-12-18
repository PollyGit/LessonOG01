import matplotlib.pyplot as plt
import numpy as np

# Создаём массив из списка. Список можно заранее записать в переменную
a = np.array([1, 2, 3, 4])
print(a)

# заполненный нулями массив 3х3
a1 = np.zeros((3, 3))
print(a1)

# заполненный единицами массив 2х5
a2 = np.ones((2, 5))
print(a2)

# заполненный рандомными числами от до 1
a3 = np.random.random((2, 5))
print(a3)

# заполненный последовательностью чисел.
# В круглых скобках указываем начало, конец и шаг:
a4 = np.arange(0, 10, 2)
print(a4)

# заполненный числами, равно распределёнными между друг другом
a5 = np.linspace(0, 1, 10)
print(a5)

# ----------------------
# построение графиков

# Генерируем массив с диапазоном значений от -10 до 10
x = np.linspace(-10, 10, 100)
# Вычисляем значение данных:
y = x ** 2

# Создаём график:
plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x**2")

# Делаем сетку на фоне графика
plt.grid(True)
plt.show()
