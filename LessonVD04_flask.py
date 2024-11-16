#Импортируем класс Flask из модуля
from flask import Flask, render_template

#Создаём переменную и сохраняем в неё объект класса Flask
#спец пременная __name__, помогает находить имя текущего модуля
app = Flask(__name__)

#Начинаем создавать функции.
# Используем декоратор из модуля Flask:
#route — конкретный декоратор, чтобы позже прописать URL-адрес страницы.
@app.route("/")
def hello_world(password=None):
    # Внутри () пишем название html-файла в кавычках
    return render_template('index.html')




#Делаем запуск. Прописываем условие проверки
if __name__ == "__main__":
    app.run()