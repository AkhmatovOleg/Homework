class Vehicle:
    vehicle_type = "None"


class Car:
    price = 1000000

    def horse_powers(self):
        return 1000


class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = "True"

    def horse_powers(self):
        return 1500


nissan1 = Nissan()
print(nissan1.vehicle_type,nissan1.price)
