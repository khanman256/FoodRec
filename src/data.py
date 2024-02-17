import json
import uuid

class DiningHall():
    def __init__(self, name, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.stations = []
        self.name = name

    def add_station(self, station):
        self.stations.append(station)
  
class Station():
    def __init__(self, name, id = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.name = name
        self.food = []
    def add_food(self, foodItem):
        self.food.append(foodItem)
    
class Food():
    def __init__(self, name, price, id=None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.name = name
        self.price = price

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

    burger = Food("Burger", 3.8)
    wrap = Food("Wrap", 5.50)
    print(burger.__dict__)

    boars_head = Station("Boars Head")
    boars_head.add_food(burger)
    boars_head.add_food(wrap)
    print(boars_head.__dict__)

    c4 = DiningHall("C4")
    c4.add_station(boars_head)
    print(c4.__dict__)

    user = User("Salaj")
    print(user.__dict__)

    rate = Rating(4)
    print(rate.__dict__)
