#ПАРСИНГ ССЫЛОК

import requests
from bs4 import BeautifulSoup

#url сайта, с которого можно взять инфу и
# не нужно использовать механизм обхода защиты для извлечения данных
# И сайты, где не надо авторизироваться
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
print(response.content)
#сохранение в переменную всей страницы
html = response.text

#указать тип парсера  - html.parser
soup = BeautifulSoup(html, 'html.parser')

#Найти и вывести в переменную все ссылки с этого сайта
#ф-ция find_all ищет все указанное на странице:
# тег "а" - ВСЕ ссылки что есть на сайте
links = soup.find_all('a')
#если написать  print(links), то неудобный формат вывода в виде списка.
# Поэтому используем цикл
for i in links:
    #указываем на атрибут 'href', чтобы получить только
    # ссылки и теги без лишней информации.
    # если print(i) - то все ссылки и теги
    print(i.get('href'))

# те ссылки что нам нужны - это синие


#-------------------

#ПАРСИНГ ЦИТАТ

url2 = 'https://randomword.com/'
response2 = requests.get(url2)
#сохранение в переменную всей страницы
html2 = response.text
#указать тип парсера  - html.parser
soup2 = BeautifulSoup(html, 'html.parser')

#Сохранить в переменную первое попавшееся(soup.find)
# или все (soup.find_all) что найдем по параметрам:
# тег 'span', класс class_='text' тк на странице F12 в теге <div>
# нужная информация (текст цитаты и автор) именно там
text = soup.find_all('span', class_='text')
print(text)
author = soup.find_all('small', class_='author')
print(author)

#теперь оформим вывод КРАСИВО
#работаем со списком, поэтому используем range
for i2 in range(len(text)):
    print(f' Цитата номер  - {i2 + 1}')
    #берем текст с сайта, там список,
    # элемент из списка с id = i2 и текст из этого элемента списка
    print(text[i2].text)
    #Вывод автора цитаты и пустую строку
    print(f' Автор цитаты - {author[i2].text}\n')



