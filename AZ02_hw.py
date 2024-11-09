import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Mark', 'Jared', 'Dean', 'Tom', 'Mary'],
    'math': [5, 4, 3, 5, 5, 5, 3, 3, 5, 3],
    'history': [5, 5, 3, 4, 4, 5, 5, 3, 5, 3],
    'language': [4, 3, 5, 5, 4, 5, 3, 4, 5, 4],
    'literature': [5, 4, 5, 5, 3, 3, 5, 5, 5, 3],
    'geography': [4, 4, 4, 5, 4, 4, 4, 5, 4, 5]
}

#создайте DataFrame с данными
df = pd.DataFrame(data)

#Выведите первые несколько строк
print(df.head())

#Вычислите среднюю оценку по каждому предмету
subject = df.iloc[:, 1:6]
rate = subject.mean(axis=0)
print(f'\nсредняя оценка по каждому предмету - \n{rate}')

#Вычислите медианную оценку по каждому предмету
rate = subject.median(axis=0)
print(f'\nмедианная оценка по каждому предмету - \n{rate}')

#Вычислите Q1 и Q3 для оценок по математике
Q1_math = df['math'].quantile(0.25)
Q3_math = df['math'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f'\nПервый квартиль по математике - {Q1_math},\nВторой квартиль по математике - {Q3_math},\nМежквартальный размах - {IQR}')

#Вычислите стандартное отклонение по каждому предмету
rate = subject.std(axis=0)
print(f'\nстандартное отклонение по каждому предмету - \n{rate}')





