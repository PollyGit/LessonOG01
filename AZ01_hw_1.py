#Набор данных об игроках LoL

import pandas as pd

df = pd.read_csv('AZ01_hw_player_LoL.csv')

#Выведите первые 5 строк данных
print(df.head())

#Выведите информацию о данных (.info())
print(df.info())

# статистическое описание (.describe())
print(df.describe())