from flask import render_template, request, redirect, url_for

from VD06_hw_user_form_card_app import app

# Инициализируем пустой список posts для хранения постов
posts = []


# Создаем маршрут с методами GET и POST:
@app.route("/", methods=["GET", "POST"])
def index():
    # использует метод POST, так как информация будет отправляться.
    # Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        # функция request.form извлекает значение из соответствующих полей.
        # Нужно получать информацию из VD06_makeform_blog.html
        # из name="title" и name="content"
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        # создаёт условие для проверки наличия данных в полях title и content
        if name and age:
            posts.append({'name': name, 'age': age, 'city': city, 'hobby': hobby })
            # redirect использует для обновления страницы и
            # предотвращения повторной отправки формы.
            # 'index' - название функции
            return redirect(url_for('index'))
    # возвращает отрендеренный шаблон с переданными данными постов
    return render_template('VD06_hw_card.html', posts=posts)
