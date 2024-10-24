# Задача "Банковские операции":
# Необходимо создать класс Bank со следующими свойствами:
#
# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.
#
# Методы объекта:
# Метод deposit:
# 1.Будет совершать 100 транзакций пополнения средств.
# 2.Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# 3.Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# 4.После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# 5.Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
# Метод take:
# 1.Будет совершать 100 транзакций снятия.
# 2.Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# 3.В начале должно выводится сообщение "Запрос на <случайное число>".
# 4.Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие,
# уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
# 5.Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств"
# и заблокировать поток методом acquire.
# Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
# После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".
#
# По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий,
# когда происходит попытка снятия при недостаточном балансе.

from time import sleep
from threading import Thread, Lock
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            sum_bal = randint(50, 500)
            self.balance += sum_bal
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {sum_bal}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            sum_remove = randint(50, 500)
            print(f'Запрос на {sum_remove}')
            if sum_remove <= self.balance:
                self.balance -= sum_remove
                print(f'Снятие: {sum_remove}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
