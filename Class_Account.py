#определить класс Account, имитирующий банковский счет.
# Класс должен включать атрибуты для хранения ид владельца, баланса счета,
# методы для депозита

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money >= 0:
            self.balance += money
            print(f'Вы успешно пополнили счет. Сумма на счете: {self.balance}')

    def withdraw(self, money):
        if self.balance < money:
            print(f'Недостаточно средств. Сумма на счете: {self.balance}')
        elif money<=self.balance:
            self.balance -= money
            print(f'Вы успешно сняли {money} рублей. Сумма на счете: {self.balance}')

    def allbalance(self):
        print(f'Текущий баланс: {self.balance}')


man = Account('1234567890', 600)
man.allbalance()
man.withdraw(400)
man.withdraw(300)
man.deposit(3000)