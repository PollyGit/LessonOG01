# очистка данных
# Пишем простой парсер.
# В итоге мы получим коллекцию со всеми рядами таблицы.

import requests
from bs4 import BeautifulSoup

url = "https://"

#Получаем страницу
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы

# Найдем все ряды из таблицы. Сохраним их в коллекцию rows
rows = soup.find_all("tr")
data = []

for row in rows:
    #В коллекцию cols сохраняются все ячейки из ряда row
    cols = row.find_all("td")
    # Используем укороченный вариант цикла for
    # Для удаления пробелов и других лишних символов используем функцию strip
    # col.text - получаем текст из колонки и
    # strip() - удаляем пробелы из текста
    # strip('xy') - удаляем определенные символы xy из текста
    # также для удаления можно использовать pop()
    cleaned_cols = [col.text.strip() for col in cols]
    # Чтобы удалить пробелы, оставляем ()
    # Чтобы удалить какие-то символы из начала и конца, пишем ('то-что-надо-удалить')
    # Функция append добавляет в список.
    data.append(cleaned_cols)

print(data)

#--------------------
# Как распарсить вложенные списки, двумерные массивы

data1 = [
    ['100', '200', '300'],
    ['400', '500', '600']

    ]

#создаем список,
# в котором будут все элементы двумерного масива
numbers = []
#Разбираем массив data
#Сначала построчно, потом по элементно в каждой строке
for row in data1:
    for text in row:
        number = int(text)
        numbers.append(number)

print(numbers)


#-----------------------
#Фильтрация данных

#Допустим, текстовые ячейки в двумерном массиве уже преобразовали в числа
data2 = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 130, 140]
    ]

list = []

#Также перебираем данные по строкам и столбцам(элементам)
for row in data2:
    for item in row:
        if item > 190:
            list.append(item)

print(list)


#--------------------






