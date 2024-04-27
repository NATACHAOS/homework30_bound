class House:
    """ДОМ"""

    def __init__(self):
        self.numberOfFloors = [0]

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors.append(floors)
        print(self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors(floors=10)
