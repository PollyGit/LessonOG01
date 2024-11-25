import sqlite3

#Создать подключение к БД
#Создаём переменную conn, 'Lesson_team_sqlite3_exampl.db' - название БД
conn = sqlite3.connect('Lesson_team_sqlite3_example.db')

#Создать объект курсора для выполнения действий
#Для создания объекта курсора создаём переменную
cur = conn.cursor()

#функцию, которая заставляет курсор выполнять действия.
# В круглых скобках пишем SQL-запрос
# прописываем столбцы таблицы:id,name,age
# NOT NULL - поле не пустое
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL)
""")

#Для сохранения используем следующую команду
conn.commit()

#Добавляем ещё информацию
# вставить в табл users значения VALUES (?, ?), равные ("Игорь", 25)
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
            ("Игорь", 25))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
            ("Алексей", 35))

conn.commit()


#Мы можем не только добавлять информацию в таблицу, но и взять её оттуда.
cur.execute("SELECT * FROM users")
#Вводим функцию для выведения информации:
rows = cur.fetchall()
#всё выводится по строчкам
#перебираем список rows, внутри которого кортежи
for row in rows:
    print(row)

conn.commit()

#Закрываем подключение
conn.close()