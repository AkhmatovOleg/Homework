class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = 1000

    def __str__(self):
        return '{} стоимость {} количество оборотов {}'.format(
            self.__class__.__name__, self.price, self.horse_powers)


class Nissan(Car):
    price = 5000000

    def horse_powers(self):
        self.horse_powers = 2000


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        self.horse_powers = 1500


nissan1 = Nissan()
nissan1.horse_powers()
print(nissan1)
kia1 = Kia()
kia1.horse_powers()
print(kia1)
