# Нужно обработать данные в csv файле, нужно убрать в конце
# каждой строчки ₽/мес. и преобразовать в тип данных число.

import csv

def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace('руб.', '').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'AZ03_hw_divan.csv'
output_file = 'AZ03_hw_divan_cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")
