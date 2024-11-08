#Мы будем парсить данные с сайта
# https://tomsk.hh.ru/vacancies/programmist
# и сохранять их в csv-файл.


import time # Импортируем модуль со временем
import csv  # Импортируем модуль csv
from selenium import webdriver  # Импортируем Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем браузер или driver = webdriver.Chrome()
driver = webdriver.Firefox()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://tomsk.hh.ru/vacancies/programmist"

# Открываем веб-страницу
driver.get(url)

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')))


# Находим все карточки с вакансиями с помощью названия класса
# и сохраняем в пременную vacancies
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')

# Выводим вакансии на экран
print(vacancies)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
    #Вариант с урока,не рабочий
   # try:
   #      # Находим элементы внутри вакансий по значению
   #      # Находим названия вакансии
   #      title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
   #      # Находим названия компаний
   #      company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
   #      # Находим зарплаты
   #      salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
   #      # Находим ссылку с помощью атрибута 'href'
   #      # а - тег, класс - bloko - link
   #      link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   # # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   # except:
   #     print("произошла ошибка при парсинге")
   #     continue
    #Вариант от куратора, рабочий
    try:
        # Извлечение названия и ссылки вакансии
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a[data-qa="serp-item__title"]')
        title = title_element.text
        link = title_element.get_attribute('href')

        # Извлечение названия компании
        company_element = vacancy.find_element(By.CSS_SELECTOR, 'a[data-qa="vacancy-serp__vacancy-employer"]')
        company = company_element.text

        # Извлечение зарплаты
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-compensation"]').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    # Вносим найденную информацию в список
    parsed_data.append([title, company, salary, link])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("LessonPS06_hh.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)


