# Нужно обработать данные в csv файле, нужно убрать в конце
# каждой строчки ₽/мес. и преобразовать в тип данных число.
# Вариант 1 от чатгпт

import csv


# Функция для очистки и преобразования строки в число
def clean_price(price_str):
    # Убираем лишние символы и пробелы
    cleaned = price_str.replace('₽/мес.', '').replace(' ', '').strip()
    # Преобразуем в целое число
    return int(cleaned)


# Чтение данных из существующего CSV файла и обработка цен
with open('AZ03_cian.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    # Чтение заголовка
    header = next(reader)

    # Подготовка данных для записи
    processed_data = []
    for row in reader:
        if row:  # Проверяем, что строка не пустая
            price_str = row[0]
            cleaned_price = clean_price(price_str)
            processed_data.append([cleaned_price])

# Запись обработанных данных обратно в CSV файл
with open('cleaned_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)  # Запись заголовка
    writer.writerows(processed_data)  # Запись обработанных данных
