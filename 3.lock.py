import threading, random, time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            increase = random.randint(50, 500)
            self.balance += increase
            print(f'Пополнение: {increase}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            decrease = random.randint(50, 500)
            print(f'Запрос на {decrease}')
            if decrease <= self.balance:
                self.balance -= decrease
                print(f'Снятие: {decrease}. Баланс: {self.balance}')
            elif decrease > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')