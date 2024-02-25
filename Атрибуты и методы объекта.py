class House:

    def __init__(self):
        self.numberofFloor = 10


house =House()

house.floor = 1
while house.floor < house.numberofFloor:
    house.floor += 1
print('Текущий этаж равен',house.floor)

