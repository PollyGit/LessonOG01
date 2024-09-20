from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print(f'Герой замахивается мечом')


class Bow(Weapon):
    def attack(self):
        print(f'Герой натягивает тетеву лука')


class Fighter():
    def __init__(self, name, race, weapon: Weapon):
        self.name = name
        self.race = race
        self.weapon = weapon
        print(f'{self.race} {self.name} вышел погулять')

    def change_weapon(self, weapon):
        if isinstance(weapon, Sword):
            weapon = 'меч'
        elif isinstance(weapon, Bow):
            weapon = 'лук'
        print(f'{self.race} {self.name} не долго думает и выбирает {weapon}')

    def attack_print(self):
        self.weapon.attack()
        v1 = f'Монстр побежден!'
        v2 = f'{self.name} слишком долго расчитывал удар, и монстр накостылял ему первым'
        v = [v1, v2]
        print(random.choice(v))


class Monster():
    def __init__(self, m_race):
        self.m_race = m_race
        print(f'И тут из-за куста появился кровожадный {m_race}')



#инициализация оружия
sword = Sword()
bow = Bow()
#инициализация персонажей
hero1 = Fighter('Вася', 'огр', sword)
monster1 = Monster('эльф')
#действия героя
hero1.change_weapon(Sword())
hero1.attack_print()

monster2 = Monster('леший')
hero1.change_weapon(bow)
hero1.attack_print()