
from printer import dict_printer
from room_validation import new_room_validation ,read_room_json,write_to_room_json,validation_per_key
from menu_printer import update_room_menu
from input_user import get_input
from python_validations import number_validation
from booking_db_handler import read_json_booking

def show_all_rooms():
    all_rooms = read_room_json()
    for room in all_rooms:
        dict_printer(room)

def show_room_by_id(room_id):
    all_rooms = read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            return room

def get_new_id(object):
    if object == "rooms":
        rooms = read_room_json()
        last_id = rooms[len(rooms)-1]["room_id"]
    else:
        rooms = read_json_booking()
        last_id = rooms[len(rooms)-1]["booking_id"]
    if last_id[-1] != "9":
        new = last_id[:-1] +str(int(last_id[-1]) +1)
    else:
        new = last_id[: -2] + str(int(last_id[-2] + 1))+"0"
    return new



def add_room_helper(name,difficulty,duration,min,max,price,is_active):
    if new_room_validation(name,difficulty,duration,min,max,price,is_active):
        new={
                "room_id": get_new_id("rooms"),
                "name": name,
                "difficulty": difficulty,
                "duration": int(duration),
                "min_players": int(min),
                "max_players": int(max),
                "price_per_player": int(price),
                "is_active": get_bool(is_active)}
        all_rooms = read_room_json()
        all_rooms.append(new)
        write_to_room_json(all_rooms)
        print("new room has been added")
        return

def get_bool(word):
    if word == "True":
        return bool(word)
    return bool(0)    

def update_room_helper(room_id):
    dicti ={"1":"name","2":"difficulty","3":"duration","4":"min_players","5":"max_players","6":"price_per_player","7":"is_active"}
    update_room_menu()
    pick =get_input("a pick")
    if not number_validation(pick):
        return
    new_val = get_input("entert new val")
    if pick == "4":
        room = show_room_by_id(room_id)
        if not validation_per_key(pick,new_val,max=str(room["max_players"])):
            return
        change_room(room_id,dicti[pick],new_val)
        return
    if pick == "5":
        room = show_room_by_id(room_id)
        if not validation_per_key(pick,str(room["min_players"]),max=new_val):
            return
        change_room(room_id,dicti[pick],new_val)
        return
    if not validation_per_key(pick,new_val):
        print("please enter valid options")
        return
    
    change_room(room_id,dicti[pick],new_val)
    return

def change_room(room_id,method,value):
    all_rooms = read_room_json()
    if method in {"duration","min_players","max_players","price_per_player"}:
        value = int(value)
    for room in all_rooms:
        if room["room_id"] == room_id:
            room[method] =value
            write_to_room_json(all_rooms)
            print("room has been updated")
            return

def change_active(room_id):
    all_rooms = read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            if room["is_active"]:
                room["is_active"] = False
            else:
                room["is_active"] = True
            write_to_room_json(all_rooms)
            print("activity has been changed")
            return
    print("room not found")
    return
        
        



    








if __name__ == "__main__":
    print(change_active("R001"))