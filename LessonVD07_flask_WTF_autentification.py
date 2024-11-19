from flask import Flask, render_template, redirect, url_for
# базовый класс для создания Форм
from flask_wtf import FlaskForm
# классы для создания полей внутри формы
from wtforms import StringField, SubmitField
# валидтор нужен для проверки
from wtforms.validators import DataRequired

# Создаем приложение Фласк
app = Flask(__name__)

# Создаём секретный ключ для защиты форм:
app.config['SECRET_KEY'] = 'your_secret_key'


# Определение формы
# Создаём класс для создания формы.
# Используем FlaskForm в качестве родительского класса
class NameForm(FlaskForm):
    # создаем поля для ввода (как в html но быстрее):
    # текстовый name и кнопку отправки submit.
    # validators=[DataRequired() проверяет что поле не пустое
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Создание маршрута для отображения и обработки формы.
# Создаём маршрут для главной страницы:
#  С помощью этого маршрута мы сможем и отправлять, и получать информацию
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()  # Создаём объект формы
    # Проверка того, прошла ли форма валидацию и вообще отправлена ли она
    if form.validate_on_submit():
        #  Получаем значение name из формы, информацию data из этого значения.
        #  Сохраняем в переменную
        name = form.name.data
        # Отправляем пользователя на новую страницу, передаём полученное имя
        return redirect(url_for('hello', name=name))
    return render_template('LessonVD07_flask_WTF_index.html', form=form)


# Создаём маршрут для отображения приветствия:
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run(debug=True)
