#Возьмем таблицу
# /Users/polly/Documents/GitHub/LessonOG01/AZ01_hh.csv
# Добавление строк/столбцов в датафрейм

import pandas as pd

#считываем файл
df = pd.read_csv('AZ01_hh.csv')
#Добавим к таблице столбец 'Test'
#
df['Test'] = [new for new in range(29)]

#Удалим столбцы axis=1 и Удалим строки axis=0
#inplace=True - изменения вносятся в исходный датафрейм,
#inplace=False - выводятся измененния, а оригинал НЕ меняется
df.drop('Test', axis=1, inplace=True)
#Удаление строки с указанием индекса
df.drop(28, axis=0, inplace=True)
print(df)

#-----------------
#Возьмем таблицу
# /Users/polly/Documents/GitHub/LessonOG01/AZ01_animal.csv
# Редактирование датафрейма

#считываем файл
df1 = pd.read_csv('AZ01_animal.csv')
print(df1)

#заполнить Nan нулями
df1.fillna(0, inplace=True)
print(df1)

#Удалить строки где в строках есть NaN
#df1.dropna(inplace=True)

#Группировать по характеристикам
#mean() - считает среднее значение по [] столбцу перед ней
group = df1.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

print(df1)

#-------------
data2 = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}

#Чтобы создать датафрейм, прописываем
df2 = pd.DataFrame(data2)

#Сохранение всех изменений в файл
df2.to_csv('AZ01_output.csv', index=False)