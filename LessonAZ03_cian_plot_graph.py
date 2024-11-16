# Нужно построить график гистограмму для получившихся
# цен из файла ”AZ03_cian_cleaned_prices.csv” с
# использованием модуля matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('AZ03_cian_cleaned_prices.csv')

# цены находятся в столбце с названием 'price'
prices = data['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Опционально: можно изменить размер графика
plt.hist(prices, bins=30, edgecolor='black')  # bins - количество столбцов в гистограмме

# Добавление заголовков и меток
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота появления таких квартир')

# Показать график
plt.show()