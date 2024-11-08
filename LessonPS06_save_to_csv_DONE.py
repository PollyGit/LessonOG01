import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')))

# Получение элементов вакансий
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')

# Создание списка для сохранения данных
parsed_data = []

# Проход по каждой вакансии и извлечение данных
for vacancy in vacancies:
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

    # Добавление данных в список
    parsed_data.append([title, company, salary, link])

# Закрытие драйвера
driver.quit()

# Запись данных в CSV файл
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)