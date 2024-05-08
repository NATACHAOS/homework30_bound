class House:
    """ДОМ"""

    def __init__(self):
        self.numberOfFloors = 0  # задаём атрибут этажности

    def setNewNumberOfFloors(self, floors):  # изменим атрибут этажности на floors и выведем на консоль
        self.numberOfFloors = floors
        print(self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors(floors="10")

