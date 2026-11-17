from pathlib import Path
import json
from python_validations import is_empty,number_validation
def read_room_json():
    path = Path(__file__).parent /"rooms.json"
    with open(path,"r") as json_file:
        all_rooms = json.load(json_file)
        return all_rooms

def write_to_room_json(all_list):
    path = Path(__file__).parent /"rooms.json"
    with open (path,"w") as file:
        json.dump(all_list,file,indent=2)
        return

def exsist(method,value):
    all_rooms = read_room_json()
    for room in all_rooms:
        if room[method] == value:
            return True
    return



def new_room_validation(name,difficulty,duration,min,max,price,is_active):
    if name_validation(name) and valid_dificult(difficulty) and number_validation(duration) and valid_dificult(difficulty) and valid_activity(is_active) and valid_price(price)and valid_minimu_maximum(min,max):
        return True
    return


def name_validation(name):
    if is_empty(name):
        print("name cant be empty")
        return
    if exsist("name",name):
        print("theroom elready exsist")
        return
    return True
    
def valid_dificult(pick):
    options={"Easy","Medium","Hard"}
    if pick not in options:
        print("invalid level")
        return
    return True

def valid_minimum_maximum(min,max):
    if not number_validation(min) or not number_validation(max):
        return
    if int(min) >= int(max):
        print("minimum cant be bigger or equal then maximum")
        return
    return True

def valid_price(price):
    if number_validation(price):
        return True
    return

def valid_activity(activity):
    options = {"True","False"}
    if activity not in options:
        return
    return True


def validation_per_key(method,value,max ="1"):
    if method == "1":
        return name_validation(value)
    if method == "2":
        return valid_dificult(value)
    if method == "3":
        return number_validation(value)
    if method == "4":
        return valid_minimum_maximum(value,max)
    if method == "5":
        return valid_minimum_maximum(value,max)
    if method == "6":
        return valid_price(value)
    else:
        print("no valid pick")
        return

if __name__ =="__main__":
    print(valid_minimum_maximum("3","8"))




    