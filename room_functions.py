from input_user import get_input
from room_helper import show_all_rooms,show_room_by_id,add_room_helper,update_room_helper,change_active
from room_validation import exsist
from printer import dict_printer
def print_all_rooms():
    show_all_rooms()
    return

def print_room_by_id():
    room_id = get_input("room id")
    if not exsist("room_id",room_id):
        print("room does not exsist")
        return
    dict_printer(show_room_by_id(room_id))
    return

def add_new_room():
    name = get_input("new room name")
    dificulty = get_input("room dificulty")
    min_people = get_input("minimum people in room")
    max_people = get_input("max people in room")
    duration = get_input("duration in minutes")
    price = get_input("price per player")
    activity =get_input("room activity")
    add_room_helper(name,dificulty,duration,min_people,max_people,price,activity)
    return

def update_room():
    room_id = get_input("room id you like to update")
    if not exsist("room_id",room_id):
        print("no such room")
        return
    update_room_helper(room_id)
    
def update_activity():
    room_id  =  get_input("room id you like to update")
    change_active(room_id)
    return





    

