#Резюме по уроку. Пример.
# Как обращаться к публичным, защищенным и приватным атрибутам и
# методам классов и наследуемых классов

class Car():
    def __init__(self, make, model):
        self.public_make = make     # 'публичный атрибут'
        self._protected_model = model   # 'защищенный атрибут'
        self.__private_year = 2022  #'приватный атрибут'

    def public_func(self):
        return f'Это открытый метод. Машина: {self.public_make} {self._protected_model}'

    def _protected_func(self):
        return "Это защищенный метод"

    def __private_func(self):
        return 'Это приватный метод'


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        #Можно обратиться только к открытому и защищенному атрибуту
        details = f'{self.public_make} {self._protected_model}, Батарея: {self.battery_size} kWh.'
        #нельзя напрямую обратиться к  __private_func() и  self.__private_year
        return details

#Создание экемпляра класса
tesla = ElectricCar('Tesla', 'Model S', 100)

#Доступ к открытому атрибуту и открытому методу
print(tesla.public_make)
print(tesla.public_func())

#Доступ к защищенному атрибуту (не рекомендуется, но возможно)
print(tesla._protected_model)
print(tesla._protected_func())

#Доступ к приватному атрибуту и методу невозможен напрямую.
# Но можно обойти это ограничение (не рекомендуется)
print(tesla._Car__private_year)     #Лучше не использовать такой прием