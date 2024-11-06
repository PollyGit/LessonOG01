import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

#lights = response.css('div._Ud0k')

lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(lights)
parsed_data = []

for light in lights:
    try:
        name = light.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').text
        price = light.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        url = light.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([name, price, url])

driver.quit()

with open("PS06_hw_light_2.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'цена', 'ссылка'])
    writer.writerows(parsed_data)







