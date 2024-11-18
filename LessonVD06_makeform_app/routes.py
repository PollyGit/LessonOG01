from flask import render_template, request, redirect, url_for

from LessonVD06_makeform_app import app

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
        title = request.form.get('title')
        content = request.form.get('content')
        # создаёт условие для проверки наличия данных в полях title и content
        if title and content:
            posts.append({'title': title, 'content': content})
            # redirect использует для обновления страницы и
            # предотвращения повторной отправки формы.
            # 'index' - название функции
            return redirect(url_for('index'))
    # возвращает отрендеренный шаблон с переданными данными постов
    return render_template('VD06_makeform_blog.html', posts=posts)
