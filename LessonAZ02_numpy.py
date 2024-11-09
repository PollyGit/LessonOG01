#Временные ряды

import pandas as pd
import numpy as np

#создадим даты с интервалом в один день D,
# указанием количества дат (10), стартовой точки (start)
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
#Создадим список из случайных значений
values = np.random.rand(10)

#Создадим датафрейм со словарём
df = pd.DataFrame({'Date': dates, 'Value': values})

#Установим колонку Date в качестве индекса всего датафрейма
df.set_index('Date', inplace=True)

#Ресэмплирование данных:
#изменения частоты временных рядов
#Сделаем перерывы в месяц М
#Те разъединить данные по месяцам .resample('M') и посчитать среднее значение .mean()
month = df.resample('ME').mean()

print(df)
print(month)


#-------------------
#Обработка выбросов

import matplotlib.pyplot as plt

data1 = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df1 = pd.DataFrame(data1)

# # Создадим график
# df1['value'].hist()
# plt.show()
#
# #другой вариант визуализации этих данных
df1.boxplot(column='value')
plt.show()

print(df1.describe())
#25% - Первый квартиль (Q1). Значение, ниже которого находится 25% всех значений
#50% - Второй квартиль (Q2)
#75% - Третий квартиль (Q3)
#пределим первый (Q1) и третий (Q3) квартили, используя функцию quantile()
Q1 = df1['value'].quantile(0.25)
Q3 = df1['value'].quantile(0.75)
#межквартальный размах (IQR)
IQR = Q3 - Q1

#определим нижнюю и верхнюю границы для определения выбросов
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

#Удаление выброса
#Прежде чем приступить к удалению выброса,
#закомментируем строки с графиками в коде, чтобы они не мешали работе:

#Создадим новый датафрейм без выбросов
df_new = df1[(df1['value'] >= downside) & (df1['value'] <= upside)]
# Создадим график, он уже будет без выбросов
df_new.boxplot(column='value')
plt.show()


#--------------------
#Работа с категориальными данными в Pandas

data2 = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df2 = pd.DataFrame(data2)

#Преобразуем столбцы в категориальные данные.
# Мы можем сделать категории для столбцов "gender" и "department"
df2['gender'] = df2['gender'].astype('category')
df2['department'] = df2['department'].astype('category')

#просмотреть уникальные категори
print(df2['gender'].cat.categories)
print(df2['department'].cat.categories)
#числовые коды категорий
print(df2['gender'].cat.codes)

#добавить новую категорию в department add_categories
df2['department'] = df2['department'].cat.add_categories(['Finance'])
#Чтобы увидеть изменения в датафрейме. Надо пересохранить (df2['department'] =)
print(df2['department'].cat.categories)

#удалить категорию remove_categories
df2['department'] = df2['department'].cat.remove_categories(['Finance'])
#Чтобы увидеть изменения в датафрейме. Надо пересохранить (df2['department'] =)
print(df2['department'].cat.categories)

print(df2)