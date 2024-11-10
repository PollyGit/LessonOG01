#Создай гистограмму для случайных данных,
# сгенерированных с помощью функции `numpy.random.normal`.

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1.0, size=1000)

#Создаём график гистограмму.
#Указываем интервалы
plt.hist(data, bins=100)
#Даём графику название
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Гистограма")
plt.show()


#Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand'

data1 = np.random.rand(5)
data2 = np.random.rand(5)
print(data1, data2)

#Создаём график диаграму рассеяния.
plt.scatter(data1, data2)
#Даём графику название
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("диаграмма рассеяния")
plt.show()