import random
from collect import *








def best_choice(user):
    random_hall = random.choice(dining_halls)
    random_station = random.choice(random_hall.stations)
    random_food = random.choice(random_station.food)
    return (random_food, random_station, random_hall)
