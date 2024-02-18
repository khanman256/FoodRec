"""
This file will connect the flask application with the the other util files we made.
"""
from data import *
from collect import *
# list of dining halls will be stored here
dining_halls = []

# code for testing
c4 = DiningHall("Chenango Champlain Collegiate Center", 1)

simple_servings = Station("Simple Servings")
for name, price in [("Steak", 4.50), ("Beans", 3.67), ("Chicken", 3.44)]:
    food = Food(name, price)
    simple_servings.add_food(food)



# code that fills dining halls should be here...
# for image in get_images():
#     data = image_to_text(image)
    # convert the data you get into a class 

# returns list of ids of all halls in dining_halls
def dining_hall_ids():
    dining_hall_id_list = []
    for hall in dining_halls:
        dining_hall_id_list.append(hall.id)
    return dining_hall_id_list

def get_dining_hall(dining_id):
    return DiningHall(name, dining_id)
    
    

    
# returns the list of ids of all stations in the specified dining hall
def get_station_ids(dining_hall_id):
    station_id_list = []
    for hall in dining_halls:
        if hall.id == dining_hall_id:
            for station in hall:
                station_id_list.append(station.id)
        return station_id_list
    
    print("ERROR")
    return
        


# returns all food ids 
def get_food_ids(dining_hall_id, station_id):
    food_id_list = []
    for hall in dining_halls:
        if hall.id == dining_hall_id:
            for station in hall:
                if station.id==station_id:
                    for food in hall:
                        food_id_list.append(food.id)
                return food_id_list
            


if __name__ == "__main__":
    pass
