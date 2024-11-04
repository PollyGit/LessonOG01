#Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
#1. Спрашивать у пользователя первоначальный запрос.
#2. Переходить по первоначальному запросу в Википедии.
#3. Предлагать пользователю три варианта действий:
#листать параграфы текущей статьи;
#перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#- листать параграфы статьи;
#- перейти на одну из внутренних статей.
#выйти из программы.

from selenium import webdriver
#Выводить текст с Клавиатуры
from selenium.webdriver.common.keys import Keys
#ПОиск на странице через ДОМ (DOM)
from selenium.webdriver.common.by import By
import time
import random

ask = input('Что вы хотите найти в Википедии? ')

#создаем объект браузера Хром или ФФ
browser = webdriver.Firefox()

#заходим на страницу
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

#Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(2)
#Находим окно поиска по названию ID
search_box = browser.find_element(By.ID, "searchInput")

#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys(ask)

#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(2)

#найдем первый попавшийся элемент по запросу
# и сохраним его в переменную а
a = browser.find_element(By.LINK_TEXT, ask)
#Добавляем клик на элемент
a.click()


while True:
    # Получаем текущий URL страницы
    current_url = browser.current_url
    # Выводим URL на экран
    print("Current URL:", current_url)
    browser.get(current_url)
    ask2 = int(input("Выберете, номер опции, что вы хотите сделать (1, 2 или 3):\n 1 - листать параграфы текущей статьи,\n 2 - перейти на одну из связанных страниц,\n 3 - выйти из программы\n"))

    #листать параграфы текущей статьи
    if ask2 == 1:
        #browser.get(current_url)
        # Ищем элементы с тегом <p>
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        # перебор, при котором следующая строка
        # появляется при нажатии на enter
        for i in paragraphs:
            print(i.text)
            input("Нажмите Enter, чтобы продолжить...")

    # перейти на одну из связанных страниц
    elif ask2 == 2:
        #browser.get(current_url)
        # Переменная со списком всех статей
        hatnotes = []

        # цикл будет перебирать список всех
        # получившихся элементов с тегом "div"
        for element in browser.find_elements(By.TAG_NAME, "div"):
            # Чтобы искать атрибут класса
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                # если класс = , то добавляем этот элемент в список
                hatnotes.append(element)

        print(hatnotes)
        if hatnotes:
            # выбираем рандомную ссылку из списка
            hatnote = random.choice(hatnotes)
            # Переходим по выбранной ссылке, она внутри атрибута href
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
            current_url = hatnote
        else:
            print("Связанных страниц не найдено.")



    #Закрываем браузер
    elif ask2 == 3:
        browser.quit()
        break

    else:
        print("Неверный выбор, попробуйте снова.")
