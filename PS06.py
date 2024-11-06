import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

#vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--umZA61PpMY07JVJtomBA')
print(vacancies)
parsed_data = []

for vacancy in vacancies:
    try:
        #title = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2').text
        #company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text').text
        #salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        #link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2')
        title = title_element.text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-labels--cR9OD8ZegWd3f7Mzxe6z').text
        link = title_element.get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)
