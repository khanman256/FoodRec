from hashlib import sha256
from uuid import uuid4
import json
import random

def generate_id(id):
    return id if id else str(uuid4())

class DiningHall():
    def __init__(self, name, img, id=None):
        self.id = generate_id(id)
        self.stations = []
        self.name = name
        self.img = img

    def add_station(self, station):
        self.stations.append(station)

    def json(self):
        print(type(self.stations[0]))
        obj = self.__dict__.copy()
        obj["stations"] = [s.json() for s in self.stations]
        return obj


class Station():
    def __init__(self, name, id=None):
        self.id = generate_id(id)
        self.name = name
        self.food = []
    def add_food(self, foodItem):
        self.food.append(foodItem)
        
    def json(self):
        obj = self.__dict__.copy()
        obj["food"] = [s.json() for s in self.food]
        return obj


class Food():
    def __init__(self, name, price, id=None):
        self.id = generate_id(id)
        self.name = name
        self.price = price
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if self.ratings:
            return sum([x.rating for x in self.ratings])//len(self.ratings)
        return 0

    def json(self):
        obj = self.__dict__.copy()
        obj["ratings"] = [r.json() for r in self.ratings]
        return obj

    

# TO DO: add password functionality
class User():
    def __init__(self, name, password=None, id=None):
        self.id = generate_id(id)
        self.name = name
        self.password=password
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def json(self):
        obj = self.__dict__.copy()
        obj["ratings"] = [r.json() for r in self.ratings]
        return obj
    
    def set_password(self, password):
        self.password = sha256(password.encode()).hexdigest()

    def validate_password(self, password):
        hash = sha256(password.encode()).hexdigest()
        return hash == self.password


class Rating():
    def __init__(self, rating, user_id, food_id, id=None):
        self.id = generate_id(id)
        self.rating = rating
        self.user_id = user_id
        self.food_id = food_id
    
    def json(self):
        return self.__dict__


## UTILITY FUNCTIONS

# weird issue where stations list is getting converted into dicts
def store_dining_halls(dining_halls):
    objs = []
    for hall in dining_halls:
        objs.append(hall.json())
    with open("static/dining_halls.json", 'w') as fp:
        json.dump(objs, fp) 


def load_dining_halls():
    objs = []
    halls = []
    with open("static/dining_halls.json", 'r') as fp:
        objs = json.load(fp)
    
    for hall in objs:
        new_hall = DiningHall(hall["name"], hall["img"], hall["id"])
        for s in hall["stations"]:
            new_station = Station(s["name"], s["id"])
            for f in s["food"]:
                new_food = Food(f["name"], f["price"], f["id"])
                new_station.add_food(new_food)
                for r in f["ratings"]:
                    new_rating = Rating(r["rating"], r["user_id"], r["food_id"], r["id"])
                    new_food.add_rating(new_rating)
            new_hall.add_station(new_station)
        halls.append(new_hall)
    
    return halls


def load_users():
    objs = []
    user_list = []
    with open("static/users.json", 'r') as fp:
        objs = json.load(fp)
    
    for user in objs:
        new_user = User(user['name'], user['password'], user['id'])
        for r in user['ratings']:
            new_rating = Rating(r['rating'], r['user_id'], r['food_id'], r['id'])
            new_user.add_rating(new_rating)
        user_list.append(new_user)
    return user_list

def store_users(user_list):
    objs = []
    for user in user_list:
        objs.append(user.json())
    with open("static/users.json", 'w') as fp:
        json.dump(objs, fp)

"""
Test cases for data
"""
if __name__ == "__main__":
    print(load_dining_halls())