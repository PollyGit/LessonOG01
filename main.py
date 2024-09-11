class Warior():

    def __int__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел есть')
        self.endurance += 2

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')
#        self.endurance += 2

    def info(self):
        print(f'Имя воина - {self.name}')
        print(f'Цвет волос воина - {self.hair_color}')
        print(f'Сила воина - {self.power}')
        print(f'Выносливость воина - {self.endurance}')