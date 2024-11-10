# Парсинг цен квартир на циане

# напиши код с использованием библиотеки selenium для
# парсинга цен с сайта
# https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/

import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Firefox()

# Открываем страницу с объявлениями
driver.get("https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/")

# Даём странице время на загрузку
time.sleep(5)  # Установите время в зависимости от скорости вашего интернета

# Парсим цены
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Открываем CSV файл для записи
with open('AZ03_cian.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])  # Записываем заголовок

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрываем браузер
driver.quit()
