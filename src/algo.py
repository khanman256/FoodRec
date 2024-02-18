import random
from collect import *

numItems = 20 #change later
numUsers = load_users()


def user_to_matrix(user):
    pass
# matrix = [numUsers.length][numItems]

 # Function to calculate similarity between users using cosine similarity
def cosine_similarity(user1, user2):
    numerator = sum(user1[i] * user2[i] for i in range(len(user1)))
    denominator = (sum(x ** 2 for x in user1) ** 0.5) * (sum(x ** 2 for x in user2) ** 0.5)
    return numerator / denominator if denominator != 0 else 0

# Function to generate recommendations for a user
def generate_recommendations(user_id, user_item_matrix, k=2):
    similarities = [(i, cosine_similarity(user_item_matrix[user_id], user_item_matrix[i])) for i in range(len(user_item_matrix)) if i != user_id]
    similarities.sort(key=lambda x: x[1], reverse=True)
    recommendations = []
    for neighbor_id, similarity in similarities[:k]:
        for item_id, rating in enumerate(user_item_matrix[neighbor_id]):
            if rating == 1 and user_item_matrix[user_id][item_id] == 0:
                recommendations.append(item_id)
    return recommendations



def best_choice(user):
    random_hall = random.choice(dining_halls)
    random_station = random.choice(random_hall.stations)
    random_food = random.choice(random_station.food)
    return (random_food, random_station, random_hall)
