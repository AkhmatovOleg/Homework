import random
import time
from threading import Thread
import queue


class Bulka(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            time.sleep(3)
            if random.random() > 0.9:
                self.queue.put('Подгорелая булка')
            else:
                self.queue.put('Нориальная булка')


class Kotleta(Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self):
        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get(timeout=5)
            if bulka == 'Нориальная булка':
                time.sleep(0.1)
                self.count -= 1
            print('Булок к приготовлению осталось ', self.count)


queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()