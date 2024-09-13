#Инкапсуляция.
#Публичный, защищенный и приватный уровни доступа к атрибутам.
#Как получить значение приватного атрибута

class Test():
    def __init__(self):
        self.public = 'публичный атрибут'
        self._protected = 'защищенный атрибут'
        self.__private = 'приватный атрибут'

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value


test = Test()
print(test.public)
print(test._protected)
print(test.get_private())
test.set_private('получили значение приватного атрибута')
print(test.get_private())


class Test2():
    def public_func(self):
        print('публичный метод')

    def _protected_func(self):
        print("защищенный метод")

    def __private_func(self):
        print('приватный метод')

    #тк не можем использовать приватный метод НАПРЯМУЮ
    #При этом метод test_private() можем использовать только внутри данного класса
    def test_private(self):
        self.__private_func()


test2 = Test2()
test2.public_func()
test2._protected_func()
test2.test_private()