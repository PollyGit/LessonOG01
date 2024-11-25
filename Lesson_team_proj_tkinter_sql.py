# Программа для добавления заказов и отметки выполненных заказов
#

import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Создаём базу данных. Работаем сверху, после блока импорта
# Создание БД и курсора, название столбцов
def init_db():
    conn = sqlite3.connect('Lesson_team_proj_orders.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    order_details TEXT NOT NULL,
    status TEXT NOT NULL)
    """)
    # Фиксирование изменений и закрытие БД
    conn.commit()
    conn.close()


# Создаём функцию добавления заказа.
def add_order():
    conn = sqlite3.connect('Lesson_team_proj_orders.db')
    cur = conn.cursor()
    # устанавливаем автоматическое назначение статуса ‘Новый’
    cur.execute(
        "INSERT INTO orders (customer_name, order_details, status) VALUES (?, ?, 'Новый')",
        (customer_name_entry.get(), order_details_entry.get()))
    conn.commit()
    conn.close()
    # Очищаем поля ввода
    customer_name_entry.delete(0, tk.END)
    order_details_entry.delete(0, tk.END)
    # для обновления
    view_orders()


# Создаём функцию для того, чтобы внесённые данные отображались
# в таблице в открытом окне:
def view_orders():
    # Надо очищать таблицу, поэтому добавим этот цикл:
    # и даляем переменную i
    for i in tree.get_children():
        tree.delete(i)
    conn = sqlite3.connect('Lesson_team_proj_orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    # Вставляем каждый новый ряд в конец таблицы
    # tree - пременная куда сохранена таблица
    # values=row записываем в значение - строчку row
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()


# Добавляем функцию, которая будет закрывать заказ:
def complete_order():
    selected_item = tree.selection()
    # Проверяем, выбрана ли хоть одна строка
    if selected_item:
        # Будем убирать первый элемент из выбранных
        # Поэтому индекс [0]
        # Находим id выбранного пункта =
        # Те берем 0 элемент  selected_item[0] и вытаскиваем оттуда
        # 0 значение ['values'][0] = это как раз его id
        order_id = tree.item(selected_item[0])['values'][0]
        # Подключение и курсор
        conn = sqlite3.connect('Lesson_team_proj_orders.db')
        cur = conn.cursor()
        # SET - сразу заменяем значение статуса
        # и указываем id того элемента WHERE id=?, который искали выше (order_id,)
        cur.execute("UPDATE orders SET status='Завершён' WHERE id=?", (order_id,))
        # Сохраняем, закрываем подключение к бд и Обновляем
        conn.commit()
        conn.close()
        view_orders()
    else:
        # Если ни одна строка не выбрана
        messagebox.showwarning("Предупреждение", "Выберите заказ для завершения")


# Создаём окошко интерфейса с названием ""
app = tk.Tk()
app.title("Система управления заказами")

# Добавляем надписи, которые будут появляться в окошке

# Используем функцию pack сразу, потому что надпись не нужно сохранять в переменную
tk.Label(app, text="Имя клиента").pack()
# Создаём поле для ввода имени клиента:
customer_name_entry = tk.Entry(app)
customer_name_entry.pack()

# Создаём такие же поля для ввода деталей заказа:
tk.Label(app, text="Детали заказа").pack()
order_details_entry = tk.Entry(app)
order_details_entry.pack()

# Создаём кнопку, которая будет добавлять введённые данные в таблицу
add_button = tk.Button(app, text="Добавить заказ", command=add_order)
add_button.pack()

# Добавляем кнопку Завершения заказа
complete_button = tk.Button(app, text="Завершить заказ", command=complete_order)
complete_button.pack()

# создать таблицу из колонок, которые в ней размещены
columns = ("id", "customer_name", "order_details", "status")  # просто кортеж
tree = ttk.Treeview(app, columns=columns, show="headings")  #

# Чтобы перебрать кортеж и поставить каждый его элемент в
# качестве кортежа, используем цикл for
# Получается таблица
for column in columns:
    tree.heading(column, text=column)
tree.pack()

init_db()
view_orders()

# Чтобы посмотреть, как сейчас всё выглядит, вводим команду
app.mainloop()
