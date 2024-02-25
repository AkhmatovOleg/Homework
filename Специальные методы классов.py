class House:

    def __init__(self):
        self.numbers_Of_Floors = None
        self.number_Of_Floors = 0

    def setNewNumberOfFloors(self, floors):
        print('текущий этаж', floors)
        self.numbers_Of_Floors = floors


house = House()
house.setNewNumberOfFloors(floors=10)

