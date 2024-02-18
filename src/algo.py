import random
from collect import *
from data import *



 #change later
numUsers = load_users()

def food_items():
    items = []
    for hall in dining_halls:
        for station in hall.stations:
            for food in station.food:
                items.append(food.id)
    return items

def get_user_ratings(user):
    rating_map = {}
    for rating in user.ratings:
        rating_map[rating.food_id] = rating.rating
    return rating_map

def users_to_matrix():
    items = food_items()
    matrix = {}
    for user in user_list:
        row = {}
        rating_map = get_user_ratings(user)
        for item in items:
            if item in rating_map:
                row[item] = rating_map[item]
            else:
                row[item] = 0
        matrix[user.id] = row
    return matrix


# Function to calculate similarity between users using cosine similarity
def cosine_similarity(user1, user2):
    numerator = sum(user1[i] * user2[i] for i in user1)
    denominator = (sum(user1[x] ** 2 for x in user1) ** 0.5) * (sum(user2[x] ** 2 for x in user2) ** 0.5)
    return numerator / denominator if denominator != 0 else 0

# Function to generate recommendations for a user
def generate_recommendations(user_id, user_item_matrix, k=2):
    similarities = [(i, cosine_similarity(user_item_matrix[user_id], user_item_matrix[i])) for i in user_item_matrix if i != user_id]
    similarities.sort(key=lambda x: x[1], reverse=True)

    for user_id, sim in similarities:
        rating_map = get_user_ratings(get_user_from_id(user_id))
        if rating_map:
            return random.choice(list(rating_map.items()))


def best_choice(user):
    best_id = generate_recommendations(user.id, users_to_matrix())[0]
    for hall in dining_halls:
        for station in hall.stations:
            for food in station.food:
                if food.id ==  best_id:
                    return (food, station, hall)