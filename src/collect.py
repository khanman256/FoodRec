from numpy import true_divide
from data import *

# list of dining halls will be stored here
dining_halls = load_dining_halls()
user_list = load_users()

### UTIL FUNCTIONS

# returns list of ids of all halls in dining_halls
def dining_hall_ids():
    dining_hall_id_list = []
    for hall in dining_halls:
        print(type(hall))
        dining_hall_id_list.append(hall.id)
    return dining_hall_id_list

def get_dining_hall(dining_id):
    for hall in dining_halls:
        if hall.id == dining_id:
            return hall
    raise Exception("Dining Hall Doesnt Exist")

def get_food_from_id(food_id):
    for hall in dining_halls:
        for stations in hall.stations:
            for f in stations.food:
                if f.id == food_id:
                    return f

def get_user_from_name(username):
    for user in user_list:
        if user.name == username:
            return user

def get_user_from_id(id):
    for user in user_list:
        if user.id == id:
            return user
        
# make sure the new user is valid before adding
def add_user(new_user):
    user_list.append(new_user)
    store_users(user_list)

def does_user_exist(username):
    username = username.lower()
    for user in user_list:
        if user.name == username:
            return True
    return False

def user_can_rate_food(user_id, food_id):
    user = get_user_from_id(user_id)
    for rating in user.ratings:
        if rating.food_id == food_id:
            return False
    return True

def add_rating(user_id, food_id, rating):
    new_rating = Rating(rating, user_id, food_id)
    user = get_user_from_id(user_id)
    user.add_rating(new_rating)
    food = get_food_from_id(food_id)
    food.add_rating(new_rating)
    store_dining_halls(dining_halls)
    store_users(user_list)

