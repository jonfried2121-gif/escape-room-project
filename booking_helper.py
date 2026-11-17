
from datetime import datetime, timedelta
from booking_validation import valid_name,valid_room,date_validator,start_check,members_check,check_room_available_time,read_json_booking,write_to_json_booking,is_cancelled
from input_user import get_input
from booking_validation import read_room_json
from printer import dict_printer,list_printer
from room_helper import get_new_id
from menu_printer import change_booking_menu
from python_validations import number_validation
from room_helper import show_room_by_id

def new_booking_validator(name,room_id,date,start,players):
    if valid_name(name) and valid_room(room_id) and date_validator(date) and start_check(start) and members_check(players,room_id) and check_room_available_time(date,start,room_id):
        return True
    return

def new_order_to_json(name,room,date,start,players):
    all_bookings = read_json_booking()
    new =  {
        "booking_id": get_new_id("booking"),
        "customer_name": name,
        "room_id": room,
        "booking_date":date ,
        "start_time": start,
        "players": int(players),
        "total_price":get_total(int(players),room,date),
        "status": "Active",
        "cancellation_fee": 0.0}
    all_bookings.append(new)
    write_to_json_booking(all_bookings)
    return
    

def get_date():
    flagg = True
    while flagg:
        year = int(get_input("year"))
        month = int(get_input("month"))
        day = int(get_input("day"))
        try:
            date =datetime(year=year,month=month,day =day)
            return date
        except Exception:
            continue

def get_start():
    hour = get_input("enter hour")
    return datetime.strptime(hour,"%H:%M")


def weekend_fee(date:datetime):
    day = datetime.strptime(date,"%Y-%m-%d")
    if day.weekday() in (5,6):
        return True
    return False
    

def get_total(people,room_id,date):
    per_one = get_per_one_price(room_id)
    price = people * per_one
    if people >= 1 and people < 4:
        return persent_calculator(0,price,date)
    if people >= 5 and people <= 6:
        total = persent_calculator(10,price,date)
        return total
    if people >= 7:
        total = persent_calculator(15,price,date)
        return total
    else:
        print("no valid number of people")
        return
    

def get_per_one_price(room_id):
    all_rooms =  read_room_json()
    for room in all_rooms:
        if room["room_id"] == room_id:
            per_one = room["price_per_player"]
            return per_one

def persent_calculator(percent,price,date):
    if weekend_fee(date):
        total =round(price-( price / 100 * percent) * 1.10)
    else:
        total = round(price-( price / 100 * percent))
    return total

def get_all_booking():
    all_bookings = read_json_booking()
    show_booking_list(all_bookings)
    return


def show_booking_list(booking):
    for book in booking:
        dict_printer(book)
    return

def get_by_id(value):
    all_bookings = read_json_booking()
    for book in all_bookings:
        if book["booking_id"] == value:
            return book
    print("error: not found")
    return

def show_by_method_operator(method,value):
    results = get_by_method(method,value)
    if not results:
        return
    return results

def get_by_method(method, value):
    results =[]
    bookings = read_json_booking()
    for book in bookings:
        if book[method] == value:
            results.append(book)
    if results == []:
        print("no books on this name or date")
        return
    return results

def is_active_room(room_id):
    room = show_room_by_id(room_id)
    if not room["is_active"]:
        print("the room is not active anymore")
        return
    return True


def change_booking_operator(book):
    
    all_books = read_json_booking()
    i = all_books.index(book)
    copy = all_books.pop(i)
    write_to_json_booking(all_books)

    if not is_active_room(book["room_id"]):
        return_old_book_to_json(i,copy)
        return
    
    flag = True
    while flag:
        change_booking_menu()
        pick = get_input("a number")
        if not number_validation(pick):
            print("pick a valid number")
            continue
        if pick == "1":
           if not change_date(copy):
                return_old_book_to_json(i,copy)
                return
            
        if pick =="2":
           if not change_start(copy):
               return_old_book_to_json(i,copy)
               return
        
        if pick == "3":
            if not change_people(copy):
                return_old_book_to_json(i,copy)
                return
        if pick =="4":
            flag = False

        print("please enter a valid number")
        continue

         
           


            


def change_date_validator(new_date:datetime.date,start,room_id):
    if date_validator(new_date) and check_room_available_time(new_date,start,room_id):
        return True
    return


def change_in_booking(copy:dict,method,value):
    print(copy)
    copy[method] = value
    new_order_to_json(copy["customer_name"],copy["room_id"],copy["booking_date"],copy["start_time"],copy["players"])
    return True

def change_start_validation(new_start:datetime,date:datetime,room_id):
    if start_check(new_start) and check_room_available_time(date,new_start,room_id):
        return True
    return

def change_people_validation(room_id,new_people):
    if members_check(new_people,room_id):
        return True
    return
  
def change_date(book):
    date = get_date()
    start = datetime.strptime(book["start_time"], "%H:%M").time()
    if not change_date_validator(date,start,book["room_id"]):
        print("oops invalid time")
        return
    date = date.strftime("%Y-%m-%d")
    change_in_booking(book,"booking_date",date)
    print("date has changed succefsully")
    return True

def change_start(book:dict):
    new_start  = get_start()
    date = datetime.strptime(book["booking_date"], "%Y-%m-%d")
    if not change_start_validation(new_start,date,book["room_id"]):
        print("oops cant change start time")
        return
    new_start = new_start.strftime("%H:%M")
    change_in_booking(book,"start_time",new_start)
    print("start time changed succesfully")
    return True

def change_people(book:dict):
    new_people = get_input("new people quantity")
    room_id = book["room_id"]
    if not change_people_validation(room_id,new_people):
        print("oops cant change members")
        return
    change_in_booking(book,"members",int(new_people))
    return True

def return_old_book_to_json(i,copy):
    all_books = read_json_booking()
    all_books.insert(i,copy)
    write_to_json_booking(all_books)
    return

def calculate_cancellation_fee(date:datetime,start:datetime,price):
    combine= datetime.combine(date.date(),start.time())
    now =datetime.now()
    if combine  - timedelta(hours= 24) > now:
        return 0
    if combine - timedelta(hours=6) > now:
        return price *0.25
    return price *0.50 

def canceltaion_operator(date,start,book_id,price):
    start = datetime.strptime(start, "%H:%M")
    date = datetime.strptime(date,"%Y-%m-%d")
    if is_cancelled(book_id):
        return
    new_price = calculate_cancellation_fee(date,start,price)
    change_booking_cancel(book_id,new_price)

def change_booking_cancel(book_id,price):
    bookings = read_json_booking()
    for book in bookings:
        if book["booking_id"] == book_id:
            book["status"] == "Cancelled"
            book["cancellation_fee"] = price
            write_to_json_booking(bookings)
            print("booking has been cancelled and updated")
            return



if __name__ =="__main__":
    print(weekend_fee("2026-7-17"))
