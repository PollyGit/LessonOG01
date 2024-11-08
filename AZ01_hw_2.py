#Определите среднюю зарплату (Salary) по городу (City)

import pandas as pd

#считываем файл
df = pd.read_csv('AZ01_dz.csv')

print(df.head())

#заполнить Nan нулями
df.fillna(0, inplace=True)

#Определите среднюю зарплату (Salary) по городу (City)
# те группируем по городу и считаем среднюю зп
group = df.groupby('City')['Salary'].mean()
print(group)

