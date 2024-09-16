#Разработай систему управления учетными записями пользователей для небольшой
# компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов
# ('admin'). Класс должен также содержать методы `add_user` и `remove_user`,
# которые позволяют добавлять и удалять пользователей из списка (представь,
# что это просто список экземпляров `User`).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
# модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
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