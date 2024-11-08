import pandas as pd

#считываем файл
df = pd.read_csv('AZ01_World-happiness-report-2024.csv')
#ф-ция .head() выводит всего первые 5 строк файла и 2 колонки
#ф-ция .head() выводит всего последние 5 строк файла и 2 колонки
print(df.head())
print(df.tail())
#info() - инфо о данных и типах
print(df.info())
#describe() - статистическая информация о данных (среднее и тд)
print(df.describe())

#вывести конкретный солбец/столбцы
print(df['Country name'])
print(df[['Country name', 'Regional indicator']])


#Вывести определенную строку с указанием ее индекса
print(df.loc[56])

#Вывести определенную ячейку с указанием
# индекса строки и названия столбца
print(df.loc[56, 'Healthy life expectancy'])

#Найти инфу по определенному условию:
#1) найти страны с показателем >0.7
print(df[df['Healthy life expectancy'] > 0.7])


#--------------------
#Series - преобразует список в столбец с индексами
data1 = [1, 2, 3, 4, 5]
series = pd.Series(data1)
print(series)

#Dataframe - табличный вид данныйх, где
# в каждой строке хранится инфо об объекта,
# а в каждом столбце одно из свойств
data2 = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}

df = pd.DataFrame(data2)
print(df)