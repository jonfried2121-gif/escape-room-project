from booking_db_handler import *
from python_validations import number_validation,is_empty
from room_validation import exsist,read_room_json
from datetime import datetime,timedelta



def valid_name(name):
    if is_empty(name):
        print("cant enter an empty stirng")
        return
    return True

def valid_room(room_id):
    if not exsist("room_id",room_id):
        print("the room does not exsist")
        return
    all_rooms = read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            if room["is_active"]:
                return True
            print("the room is unavailble")
            return



def date_validator(date:datetime):
    today = datetime.now().date()
    if today > date.date():
        print(today)
        print(date)
        print("date has already gone")
        return
    return True


def start_check(start:datetime):
    if start.time() < datetime.strptime("10:15","%H:%M").time():
        print("cant start before 10:15")
        return
    if start.time() > datetime.strptime("22:00", "%H:%M").time():
        print("cant start after 22:00")
        return
    return True
    

def members_check(people,room_id):
    if not number_validation(people):
        return
    all_rooms = read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            maximum = room["max_players"]
            minimum = room["min_players"]
    if int(people) < minimum or int(people) > maximum:
        print("no valid number of people")
        return
    return True

def check_room_available_time(date:datetime,time:datetime,room_id):
    all_bookings = read_json_booking()
    room_time = get_room_time(room_id)
    all_rooms_in_day = list(filter(lambda k : datetime.strptime(k["booking_date"],'%Y-%M-%d').date() == date.date() and k["room_id"] == room_id,all_bookings))
    if not all_rooms_in_day:
        return True
    for room in all_rooms_in_day:
        if not check_hefresh(room_time,time,datetime.strptime(room["start_time"],"%H:%M")):
            return
    return True


def check_hefresh(room_time,our_room:datetime,other_room:datetime):
    if other_room.time() > our_room.time():
        end = our_room.time()
        start = other_room.time()  
    else:
        end = other_room.time()
        start = our_room.time()
    hefresh = (start - end).total_seconds() // 60
    if hefresh < (15 + room_time):
        return
    

    

def get_room_time(room_id):
    all_rooms = read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            room_time = room["duration"]
            return room_time

def is_cancelled(book_id):
    all_bookings = read_json_booking()
    for book in all_bookings:
        if book["booking_id"] == book_id:
            return book["status"] != "Active"


def date_cancellation_validation(date:datetime):
    if not date_validator(date):
        return
    
    
        
    
    
    
        
    
    
    



        

if __name__ =="__main__":
     a= datetime.strptime("17:00", "%H:%M")
     b= datetime.strptime("2026-11-16","%Y-%m-%d")
     print(date_cancellation_validation(b,a)) 



    


        


     

