#Создайте простую текстовую боевую игру, где игрок и компьютер
# управляют героями с различными характеристиками. Игра состоит
# из раундов, в каждом раунде игроки по очереди наносят урон друг
# другу, пока у одного из героев не закончится здоровье.
from random import randint, choice

class Hero:
    def __init__(self, name, health=100, power=20):
        self.health = health
        self.power = power
        self.name = name

    def attack(self,other):
        if self.is_alive():
            self.power = randint(20, 40)
            if other.health >= self.power:
                other.health -= self.power
                return (f'{self.name} атаковал {other.name} и нанес {self.power} едениц урона. '
                        f'У {other.name} осталось {other.health} хп')
            else:
                other.health = 0
                return (f'{self.name} атаковал {other.name} и нанес {self.power} едениц урона. '
                    f'У {other.name} не осталось хп, он отдыхает. {self.name} Победил!')
        else:
            return (f'{self.name} не может атаковать {other.name}, он отдыхает')


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    # def who_wins(self, other):
        # if self.is_alive and not other.is_alive:
        #      print(f'{self.name} Победил')
        # elif other.is_alive and not self.is_alive:
        #     print(f'{other.name} Победил')
        # else:
        #     print('Битва продолжается до победного!')



#На случай, если нужно будет добавлять для классовв различные методы
class Player(Hero):
    def __init__(self, name):
        super().__init__(name)

class Computer(Hero):
    def __init__(self, name):
        super().__init__(name)


#Класс Игры
class Game:
    def start(cls):
        p3 = input('Введите имя игрока: ')
        p1 = Player(p3)
        p2 = Computer('Компьютер')
        i = 0
        # p3 = random.choice([p1, p2])
        while p1.is_alive() and p2.is_alive():
            print(f' Раунд {i}.')
            i += 1
            print(p1.attack(p2))
            temp = p1
            p1 = p2
            p2 = temp


game = Game()
game.start()