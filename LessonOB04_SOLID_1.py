#Принцип единственной ответственности
# (SRP, Single Responsibility Principle)
class User():
    def __init__(self, user):
        self.user = user

class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user = new_name

class SaveUser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open('user.txt', 'a')
        file.write(self.user)
        file.close()


#Принцип открытости/закрытости
# (OCP, Open/Closed Principle)
#Создание Абстрактных классов

#импортируем модуль для работы с абстрактными классами
from abc import ABC, abstractmethod

#создаем подкласс абстрактного класса АВС, внутри которого
# есть абстрактный метод обозначенный декоратором @abstractmethod.
#Метод пустой, тк Formatted() класс - шаблон для других классов,
# которые юудут наследоваться
class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)


class HtmlFormatted(Formatted):
    def format(self, report):
        print(f'<h1>{report.title}</h1>')
        print(f'<p>{report.content}</p>')

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)
        #обращение к методу format() разных классов через атрибут,
        # который является названием класса
        # self - сам себя передает


report = Report('заголовок отчета',
                "это текст отчета, его тут много",
                TextFormatted())
report.docPrinter()

report2 = Report('заголовок отчета html',
                "это текст отчета, его тут много",
                HtmlFormatted())
report2.docPrinter()



#Принцип подстановки Барбары Лисков
# (LSP, Liskov substitution Principle)
#При подстановке экземпляра класса Потомков вместо
# экземпляров Родительского класса программа не ломается

class Bird():
    def fly(self):
        print('it is flying')


class Duck(Bird):
    def fly(self):
        print('This duck is flying fast')


def fly_in_the_sky(animal):
    animal.fly()


b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)


#Принцип разделения интерфейсов
# (ISP, Interface Segregation Principle)
#вместо класса SmartHouse исользовать несколько тематических классов

class Light():
    def turn_on_light(self):
        print('Свет включен')


class Food():
    def heat_food(self):
        print('Еда разогревается')


class Music():
    def turn_on_music(self):
        print('Музыка включена')



#Принцип инверсии зависимости
# (DIP, Dependency Inversion Principle)
# Модули высокого уровня не должны зависеть от модулей низкого
# уровня. Оба типа модулей должны зависеть от абстракций.
from abc import ABC, abstractmethod

class StorySource(ABC):
    #класс источника информции
    #это абстрактный класс для создания шаблона
    @abstractmethod
    def get_story(self):
        pass


class Book(StorySource):
    #подкласс источника информции - Книга
    def get_story(self):
        print('Чтение интересной истории')


class AudioBook(StorySource):
    #подкласс источника информции - аудио книга
    def get_story(self):
        print('Чтение интересной истории вслух')


class StoryReader():
    def __init__(self, story_sourse: StorySource):
        self.story_sourse = story_sourse

    def tell_story(self):
        self.story_sourse.get_story()


#Создаем экземпляры классов источников (бум.книга или аудио)
book = Book()
audio = AudioBook()
#Передаем классу какой-то конкретный источник (бум.книга или аудио)
readerBook = StoryReader(book)
readerAudio = StoryReader(audio)

readerBook.tell_story()
readerAudio.tell_story()