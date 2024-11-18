from flask import Flask

# создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)

# Создаем секретный ключ для защиты данных: любая строка
# для теста обычно “you will never guess”
app.config['SECRET_KEY'] = 'your_secret_key_for_VD06_hw'

# Импортируем маршруты из директории:
from VD06_hw_user_form_card_app import routes
