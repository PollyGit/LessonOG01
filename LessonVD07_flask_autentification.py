from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Создаем приложение Фласк
app = Flask(__name__)

#Настраиваем базу данных
# Эта строчка нужна, чтобы мы могли подключиться к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# Эта строчка отключает сигнализацию об изменении объектов внутри базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Создание объекта, через который мы будем работать с базой данных
db = SQLAlchemy(app)


# Определение модели (таблицу в БД) базы данных
# Создаем класс (User-любое название)
# В скобках указываем модель db.Model, чтобы в дальнейшем
# создать именно базу данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) # В скобках описываем поля таблицы
    #id — целое число, первичный ключ.
    # username — строка длиной до 80 символов, unique=True уникальная,
    # nullable=False: не может быть пустой.

    # Этот метод __repr__ определяет, как объект модели будет
    # выглядеть в виде строки
    def __repr__(self):
        return f'<User {self.username}>'


#Создаём таблицу в базе данных:
# Функция создаёт контекст приложения, который нужен для работы с базой данных
with app.app_context():
    # Создание всей таблицы, которые определены в классе User
    db.create_all()


#Добавляем запись в таблицу
# С помощью декоратора создаём маршрут /add_user',
# который будет вызывать функцию add_user()
@app.route('/add_user')
def add_user(): # Функция будет создавать объект класса User
    new_user = User(username='new_username')
    db.session.add(new_user) # Добавляем в сессию
    # Сессия — временное хранилище перед добавлением в базу данных.
    db.session.commit() #  Сохраняем изменения в базу данных
    # Вывод сообщения о том, что юзер добавлен в базу данных
    return 'User added'


#Получение данных из базы данных
#Создаём маршрут для получения всех пользователей:
@app.route('/users')
def get_users():
    # Получаем всех юзеров из базы данных и сохраняем в переменную users
    users = User.query.all()
    return str(users)

if __name__ == "__main__":
    app.run(debug=True)