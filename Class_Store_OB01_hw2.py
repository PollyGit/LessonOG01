#создать класс `Store`, который можно будет использовать для создания различных
# магазинов. Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена.
#Методы класса:
#- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
#-  метод для добавления товара в ассортимент.
#- метод для удаления товара из ассортимента.
#- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
#- метод для обновления цены товара.

class Store():
    def __init__(self, name, address, items=None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_to_store(self, tag, price):
        self.items[tag] = price

    def remove_from_store(self, tag):
        del self.items[tag]

    def get_price(self, tag):
        print(f'Цена товара {tag} : {self.items.get(tag)}')

    def update_price(self, tag, new_price):
        self.items[tag] = new_price
        print(f'Новая цена товара {tag}: {new_price}')

store_car = Store('BMW', 'store_car.com')
store_apteka = Store('Aibolit', 'store_apteka.com')
store_food = Store('EDA', 'store_food')

store_car.add_to_store('X3', 45000)
store_car.add_to_store('X5', 49000)
store_car.add_to_store('X7', 53000)
print(store_car.items)

store_apteka.add_to_store('Nurofen', 460)
store_apteka.add_to_store('Vitamin C', 900)
store_apteka.add_to_store('MgB6', 1450)
print(store_apteka.items)

store_food.add_to_store('Milk', 80)
store_food.add_to_store('Cookies', 180)
store_food.add_to_store('Avokado', 360)
print(store_food.items)

store_food.add_to_store('KitKat', 60)
print(store_food.items)

store_food.get_price('KitKat')
store_food.update_price('Milk', 104)
store_food.remove_from_store('KitKat')
print(store_food.items)