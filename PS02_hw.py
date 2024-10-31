# Задание 1: Получение данных

import requests
import pprint

# Отправьте GET-запрос с параметром html
params = {
    'q': 'html'
}

response = requests.get('https://api.github.com',
                        params=params)

# Распечатайте статус-код ответа
print(response.status_code)

# Распечатайте содержимое ответа в формате JSON
response_json = response.json()
pprint.pprint(response_json)

# Задание 2: Параметры запрос

# Отправьте GET-запрос с параметром `userId`, равным `1`
params2 = {
    'userId': 1
}

# Используйте API, который позволяет фильтрацию данных через URL-параметры
url = 'https://jsonplaceholder.typicode.com/posts'
response2 = requests.get(url, params=params2)

# Распечатайте полученные записи
if response2.status_code >= 200 & response2.status_code < 400:
    print(response2.text)
else:
    print('Произошла ошибка')

# Задание 3: Отправка данных
url2 = 'https://jsonplaceholder.typicode.com/posts'

# Создайте словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправьте POST-запрос с этими данными
response3 = requests.post(url2, data=data)

# Распечатайте статус-код и содержимое ответа
print(f'Статус-код: {response3.status_code}')
print(f'Содержимое ответа: {response3.json()}')
