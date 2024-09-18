
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} is eating')


class Bird(Animal):
    def make_sound(self):
        print('fewfew')


class Reptile(Animal):
    def make_sound(self):
        print('shhhsshs')


class Mammal(Animal):
    def make_sound(self):
        print('gav')


#вызывает звук каждого конкретного животного из списка
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo():
    def __init__(self):
        self.human_list = []
        self.animal_list = []

    def add_animal(self, animal):
        self.animal_list.append(animal)
        print(f'Animal {animal.name} is added to the Zoo')

    def add_human(self, new_staff):
        self.human_list.append(new_staff)
        print(f'Human {new_staff} is added to the Zoo')


class Zookeeper:
    def feed_animal(self, animal):
        print(f'Zookeeper feeds the {animal.name}.')


class Veterinarian:
    def heal_animal(self, animal):
        print(f'Veterinarian heals the {animal.name}. The {animal.name} is ill.')



# инициализация экземпляров класса животных
bird1 = Bird('hawk', 2)
bird2 = Bird('pigeon', 0.2)
reptile1 = Reptile('lizard', 3)
mammals1 = Mammal('elephant', 32)
mammals2 = Mammal('mouse', 1)

zoo = Zoo()
zookeeper1 = Zookeeper()
veterinarian1 = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(reptile1)
zoo.add_animal(mammals1)
zoo.add_human(zookeeper1)
zoo.add_human(veterinarian1)

animal_sound(zoo.animal_list)

zookeeper1.feed_animal(bird1)
veterinarian1.heal_animal(mammals1)