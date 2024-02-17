"""
This file will connect the flask application with the the other util files we made.
"""
from data import *

# list of dining halls will be stored here
dining_halls = []

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
def get_food_ids(station_id):
    pass


if __name__ == "__main__":
    c4 = DiningHall("Chempad 3jldkfjs")
    

"""
-get file path, send to image scn
-write tests
"""