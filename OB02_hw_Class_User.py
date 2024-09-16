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

class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access_level = 'user'

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, value):
        if value != 'user' or value != 'admin':
            print('this access level is denied')
        else:
            self._access_level = value

    def __str__(self):
        return f"{self._id}, {self._name}"


class Admin(User):
    user_list = []
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access_level = 'admin'

    @classmethod
    def add_user(cls, user):
        if isinstance(user, User) and user not in cls.user_list:
            cls.user_list.append(user)
        else:
            print('user doesn`t exist or is found in list')

    @classmethod
    def remove_user(cls, user):
        if isinstance(user, User) and user in cls.user_list:
            cls.user_list.remove(user)
        else:
            print('user is not found')

    @classmethod
    def print_list(cls):
        for i in cls.user_list:
            print(i)


#СОздание юзеров и админов
user1 = User(111, 'Vasya')
user2 = User(112, 'Stepa')
user3 = User(113, 'Masha')
user4 = User(114, 'Bobby')
user5 = User(115, 'Harry')
user6 = User(116, 'Georg')
admin1 = Admin(222, 'Misha')

#Добавление юзеров
admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin1.add_user(user4)
admin1.add_user(user5)
admin1.add_user(user6)

#Повторное добавление юзера, который уже есть
admin1.add_user(user2)

#Удаление юзера из списка
admin1.remove_user(user3)

#Вывод списка юзеров построчно
admin1.print_list()