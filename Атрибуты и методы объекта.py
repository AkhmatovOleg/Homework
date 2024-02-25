class House:

    def __init__(self):
        self.number_of_Floor = 10


house =House()

house.floor = 1
while house.floor < house.number_of_Floor:
    house.floor += 1
print('Текущий этаж равен',house.floor)

