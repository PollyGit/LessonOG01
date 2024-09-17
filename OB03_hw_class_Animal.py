#Создайте базовый класс `Animal` с атрибутами `name`, `age` и методами `make_sound()`, `eat()`
# для всех животных. Создать подклассы `Bird`, `Mammal`, и `Reptile` и переопределить `make_sound().
# Создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод
# `make_sound()` для каждого животного. Создать класс `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# Создать классы для сотрудников `ZooKeeper`, `Veterinarian`с методами `feed_animal()` `heal_animal()`.
# Дополнительно:
# (не сделано) Доп функции :сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего
# зоопарка было "постоянное состояние" между запусками программы.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} is eating {self.food}')

    # Метод `__repr__` переопределен для удобного отображения объектов при печати.
    def __repr__(self):
        f"Animal({self.name}, {self.age})"


class Bird(Animal):
    bird_list = []

    def __init__(self, name, age, color, food):
        super().__init__(name, age)
        self.color = color
        self.food = food
        Bird.bird_list.append(self)

    def make_sound(self):
        return 'fewfew'

    def __repr__(self):
        return f"Bird({self.name})"


class Reptile(Animal):
    reptile_list = []

    def __init__(self, name, age, color, food):
        super().__init__(name, age, )
        self.color = color
        self.food = food
        Reptile.reptile_list.append(self)

    def make_sound(self):
        return 'shhhsshs'

    def __repr__(self):
        return f"Reptile({self.name})"


class Mammal(Animal):
    mammal_list = []

    def __init__(self, name, age, sound, food):
        super().__init__(name, age, )
        self.sound = sound
        self.food = food
        Mammal.mammal_list.append(self)

    def make_sound(self):
        return f'{self.sound}'

    # Метод `__repr__` переопределен для удобного отображения объектов при печати.
    def __repr__(self):
        return f"Mammals({self.name})"


def print_sound(animal):
    print(f'{animal.name} says {animal.make_sound()}')


class Zookeeper:
    zookeeper_list = []

    def __init__(self, name):
        self.name = name
        Zookeeper.zookeeper_list.append(self)

    def feed_animal(self, animal):
        self.animal = animal
        print(f'Zookeeper {self.name} feeds the {animal.name} with {animal.food}.')

    # Метод `__repr__` переопределен для удобного отображения объектов при печати.
    def __repr__(self):
        return f"Zookeeper({self.name})"


class Veterinarian:
    veterinarian_list = []

    def __init__(self, name):
        self.name = name
        Veterinarian.veterinarian_list.append(self)

    def heal_animal(self, animal):
        self.animal = animal
        print(f'Veterinarian {self.name} heals the {animal.name}. The {animal.name} is ill.')

    # Метод `__repr__` переопределен для удобного отображения объектов при печати.
    def __repr__(self):
        return f"Veterinarian({self.name})"


class Zoo:
    human_list = []
    animal_list = []

    @classmethod
    def add_to_human_list(cls, human):
        if (isinstance(human, Veterinarian) or isinstance(human, Zookeeper)) and (human not in cls.human_list):
            cls.human_list.append(human.name)
        else:
            print('user doesn`t exist or is found in list')
        return f'All humans: {cls.human_list}'

    # 1й вариант вывести весь список сотрудников
    @classmethod
    def type_human_list(cls):
        print(f'All humans {cls.human_list}')

    @classmethod
    # 2й вариант вывести весь список сотрудников
    def common_human_list(cls):
        human_list2 = [*Veterinarian.veterinarian_list, *Zookeeper.zookeeper_list]
        print(human_list2)

    @classmethod
    def common_animal_list(cls):
        animal_list = [*Bird.bird_list, *Reptile.reptile_list, *Mammal.mammal_list]
        print(animal_list)


# инициализация экземпляров класса животных
bird1 = Bird('hawk', 2, 'brown', 'worms')
bird2 = Bird('pigeon', 0.2, 'gray', 'bread')

reptile1 = Reptile('lizard', 3, 'multicolor', 'bugs')

mammals1 = Mammal('elephant', 32, 'yiiii', 'vegetables')
mammals2 = Mammal('mouse', 32, 'pipipi', 'cheese')

# Основные действия экземпляров животных классов
print_sound(bird1)
bird1.eat()

print_sound(reptile1)
reptile1.eat()

print_sound(mammals2)
mammals2.eat()

# Инициализация сотрудников
zookeeper1 = Zookeeper('Vasya')
zookeeper2 = Zookeeper('Bob')
zookeeper1.feed_animal(bird2)

veterinarian1 = Veterinarian('Petya')
veterinarian1.heal_animal(mammals1)

# добавление сотрудника в общий список сотрудников Зоопарка
Zoo.add_to_human_list(zookeeper1)
Zoo.add_to_human_list(zookeeper2)
Zoo.add_to_human_list(veterinarian1)

# вывод список сотрудников по классам
# print(Zoo.human_list)
print(Zookeeper.zookeeper_list)
print(Veterinarian.veterinarian_list)

# Вывод общего списка сотрудников Зоопарка, 2 способа:
Zoo.type_human_list()
Zoo.common_human_list()
# Вывод общего списка животных
Zoo.common_animal_list()
