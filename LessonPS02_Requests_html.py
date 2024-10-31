import requests
import pprint

#запрос
# response = requests.get('https://www.google.com')
# #код статуса запроса
# print(response.status_code)
##вывод заголовка
# print(response.headers)
# # True - статус от 200 до 400, False - статус от 400
# print(response.ok)
#
# if response.ok:
#     print('Запрос успешно выполнен')
# else:
#     print('Произошла ошибка')
#
# #выводится вся страница по запросу get в юникоде
# print(response.text)
# #если результат запроса - файл, а не страница,
# # то вместо text использовать content
# print(response.content)

# response2 = requests.get('https://api.github.com')
# #вывод в формате json
# #pprint - ф-ция для чтения словарей
# response2_json = response2.json()
# print(response2_json) #обычный формат
# pprint.pprint(response2_json) #удобный формат

#-----------------

# #создание библиотеки-словаря
# #поисковый запрос python
# #q - ключ словаря query
# params = {
#     'q': 'python'
# }
#
# #первый params- атрибут ф-ции get,
# # а второй params-имя созданной библиотеки
# response = requests.get('https://api.github.com/search/repositories',
#                         params=params)
#
# response_json = response.json()
# pprint.pprint(response_json)
#
# #вывод количества результатов поиска по
# # ключу 'total_count' словаря response_json
# print(f'Количество репозиториев с использованием python : {response_json['total_count']}')


#-----------------

# #Скачаем изображение из группы Вконтакте также при помощи get-запроса
# import requests
#
# img = 'https://sun9-13.userapi.com/impg/spGAlQ6qPcRP7qzCFCZXcsQvRV1hX2U_k74o9w/RLhqunrYUbo.jpg?size=1280x851&quality=95&sign=0c5a66beaab6cee8b0e8732f667a3a9d&type=album'
# response = requests.get(img)
#
# #открыть файл → записать туда информацию → закрыть файл
# #w — для записи
# #b — бинарный режим
# with open('test.jpg', 'wb') as file:
#     file.write(response.content)
#     #записать контент(инфу), который сохранился в response


#-----------------
#Отправка данных на сервер
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'тестовый запрос',
    'body': 'тестовый контент post запроса',
    'userId': 2
}
response = requests.post(url, data=data)

print(response.status_code)

print(f'ответ - {response.json()}')

