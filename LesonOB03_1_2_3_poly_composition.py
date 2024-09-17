# Полиморфизм
class Animal():
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('gav')


class Cat(Animal):
    def make_sound(self):
        print('meow')


class Cow(Animal):
    def make_sound(self):
        print('mumu')


# список классов
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()


# gav
# meow
# mumu


# Полиморфизм
class Shape():
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


def print_area(shape):
    print(f'Площадь фигуры - {shape.area()}')


circle_1 = Circle(5)
print_area(circle_1)
square_1 = Square(7)
print_area(square_1)
rectangle_1 = Rectangle(3, 6)
print_area(rectangle_1)


# Композиция и Агрегация
class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Агрегация

    def get_info_book(self):
        print(f'"{self.title}", {self.author.name}')


author1 = Author('Лев Толстой', 'русский')
book1 = Book('Война и мир', author1)
print(book1.author.name)
book1.get_info_book()
