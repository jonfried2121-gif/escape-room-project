
from room_helper import show_room_by_id
from booking_db_handler import read_json_booking
from printer import dict_printer
from booking_helper import show_by_method_operator

def number_all_orders_active(all_bookings:list):
    return len(list(filter(lambda k : k["status"] == "Active",all_bookings)))


def number_of_all_cancelled(all_booking:list):
    return len(all_booking) - number_all_orders_active(all_booking)

def all_income(all_booking:list):
    revenue = 0
    active_list = list(filter(lambda k : k["status"] == "Active",all_booking))
    for book in active_list:
        revenue += book["total_price"]
    return revenue

def most_popular_room(bookings):
    dictionary={}
    active_list = list(filter(lambda k : k["status"] == "Active",bookings))

    for book in active_list:
        if book["room_id"] in dictionary:
            dictionary[book["room_id"]] += 1
        else:
            dictionary[book["room_id"]] = 1

    room_id= max(dictionary,key = dictionary.get)
    return show_room_by_id(room_id)["name"]


def number_of_bookings_per_room(bookings):
    dictionary={}
    for book in bookings:
        if book["room_id"] not in dictionary:
            dictionary[book["room_id"]] = 1
        else:
             dictionary[book["room_id"]] += 1
    name_bookings ={}
    for key, value in dictionary.items():
        name_bookings[show_room_by_id(key)["name"]] = value
    dict_printer(name_bookings)
    return

def persent_capacity_by_room(room_id,date):
    sum_people = 0
    room = show_room_by_id(room_id)
    all_bookings = show_by_method_operator("booking_date",date)
    maximum_today = room["max_players"] * len(all_bookings)
    for book in all_bookings:
        sum_people += book["players"]
    return sum_people / maximum_today * 100


if __name__ == "__main__":
    all_bookings  = read_json_booking()
    print(persent_capacity_by_room("R003","2026-11-17"))




    
