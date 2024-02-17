import json
import uuid

class DiningHall():
    def __init__(self, name, id = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        pass
        self.name = name
    def add_station(self, station):
        hallStation = []
        hallStation.append(station)

    
class Station():
    def __init__(self, name, id = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        pass
        self.name = name
    def add_food(self, foodItem):
        stationFood = []
        stationFood.append(foodItem)
    
class Food():
    def __init__(self, name, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.name = name

class User():
    def __init__(self, name, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.name = name
    
class Rating():
    def __init__(self, rating, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.rating = rating


        

"""
Test cases for data
"""
if __name__ == "__main__":

    # burger = Food("Burger")
    # wrap = Food("Wrap")
    # print(burger.__dict__)

    # boars_head = Station("Boars Head")
    # boars_head.add_food(burger)
    # boars_head.add_food(wrap)
    # print(boars_head.__dict__)

    # c4 = DiningHall("C4")
    # c4.add_station(boars_head)
    # print(c4.__dict__)

    user = User("Salaj")
    
