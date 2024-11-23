# импортируем Flask и библиотеку Request
import requests
from flask import Flask, render_template, request

# импортируем объект класса Flask
app = Flask(__name__)


# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
# создаем функцию с переменной weather, где мы будем сохранять погоду
# И изначально задаем их пустыми
def index():
    weather = None
    news = None
    quote = None

    # формируем условия для проверки метода.
    # Форму мы пока не создавали, но нам из неё необходимо
    # будет взять только город.
    if request.method == 'POST':
        # этот определенный город мы будем брать для запроса API
        city = request.form['city']
        # прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
        weather = get_weather(city)
        news = get_news()
        quote = get_quotes()
        # передаем информацию о погоде и новостях в index.html
    return render_template("index.html", weather=weather, news=news, quote=quote)


# Функцияя index не взаимодействует с API,
# поэтому следующим шагом мы пропишем функцию,
# которая будет взаимодействовать с API и брать информацибю о погоде.

# в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
    # личный апи ключ с сайта
    api_key = "5fb8a70540bf235e17b9556ef1daa937"
    # адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат json возврата результата
    return response.json()


#Создаём переменную для получения новостей и вставляем ключ:
def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   #Если ключа articles не будет, возвращаться будет пустой список
   return response.json().get('articles', [])


def get_quotes():
    api_key = "6dc59447865c8be9b2546779546467dd"
    headers = {
        'Authorization': f'Token token="{api_key}"'
    }
    url = f"https://favqs.com/api/qotd"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('quote', {})


# Прописываем запуск для проверки приложения
if __name__ == '__main__':
    app.run(debug=True)
