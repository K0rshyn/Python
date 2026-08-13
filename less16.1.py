class Kassa(object):
    def __init__(self, b):
        self.balance = b
    def top_up(self, x = None):
        if x is None:
            while True:
                try:
                    x = int(input("Введите сумму, на которую хотите пополнить баланс: "))
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
        self.balance += x
        print(f"Баланс пополнен на {x}. Текущий баланс: {self.balance}")
    def count_1000(self):
        c = self.balance // 1000
        print(f'На данный момент на балансе {c} целых тысяч')
    def take_away(self, x = None):
        x = int(input("Введите сумму, которую хотите снять со счёта: "))
        if x <= self.balance:
            self.balance -= x
            print(f"Вы сняли со счёта: {x}. На Вашем балансе осталось: {self.balance}")
            return
        else:
            print(f"На Вашем счёте не достаточно средств. Ваш баланс: {self.balance}")
kazna = Kassa(5000)
kazna.top_up()
print(kazna.balance)
kazna.count_1000()
kazna.take_away()
