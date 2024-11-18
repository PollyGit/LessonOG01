from flask import Flask

#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)

#Создаем секретный ключ для защиты данных: любая строка
#для теста обычно “you will never guess”
app.config['SECRET_KEY'] = 'your_secret_key'

#Импортируем маршруты из директории:
from LessonVD06_makeform_app import routes
