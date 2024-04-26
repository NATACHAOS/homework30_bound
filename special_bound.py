class House:
    """ДОМ"""

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, item):
        print(self.numberOfFloors)
        print(item)


my_house = House()
my_house.setNewNumberOfFloors(item='floors')
