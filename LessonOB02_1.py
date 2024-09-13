#Lesson OG02_1
#тема НАСЛЕДОВАНИЕ

class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} is flying')

    def eat(self):
        print(f'{self.name} is eating')

    def sing(self):
        print(f'{self.name} is singing')

    def info(self):
        print(f'{self.name} is name')
        print(f'{self.voice} is voice')
        print(f'{self.color} is color')

class Pigeon(Bird):
    def __init__(self, name, voice, color, favourite_food):
       # метод super() позволяет обращаться к методам родительского класса из дочернего
       super().__init__(name, voice, color)
       self.favourite_food = favourite_food

    def sing(self):
        print(f'{self.name} is singind kyrlik kyrlik')

    def walk(self):
        print(f'{self.name} is walking')


bird1 = Pigeon("Gosha", "kyrlik", "grey", 'bread')

bird1.info()
bird1.walk()
bird1.sing()

bird2 = Bird('Masha', 'chik', 'brown')

bird2.fly()