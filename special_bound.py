class House:
    """ДОМ"""

    def __init__(self):
        self.numberOfFloors = 0 # задаём атрибут этажности

    def setNewNumberOfFloors(self):  # изменим атрибут этажности на floors и выведем на консоль
        self.floors = floors = 10
        self.numberOfFloors = floors
        print(self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors()
