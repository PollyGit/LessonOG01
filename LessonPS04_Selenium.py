from selenium import webdriver
# Выводить текст с Клавиатуры
from selenium.webdriver import Keys
# ПОиск на странице через ДОМ (DOM)
from selenium.webdriver.common.by import By
import time

# создаем объект браузера Хром или ФФ
# browser = webdriver.Chrome()
browser = webdriver.Firefox()

# заходим на страницу https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0
browser.get(
    "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# #Ищем элементы с тегом <p>
# paragraphs = browser.find_elements(By.TAG_NAME, 'p')
# #перебор, при котором следующая строка
# # появляется при нажатии на enter
# for i in paragraphs:
#     print(i.text)
#     #input() пустой, чтобы при нажатии на enter
#     # выводился следующий параграф
#     input()

# -----------------
import random

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
# выбираем рандомную ссылку из списка
hatnote = random.choice(hatnotes)
# Переходим по выбранной ссылке, она внутри атрибута href
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(15)
