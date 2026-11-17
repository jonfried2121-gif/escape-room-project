from input_user import get_input
from booking_helper import  get_date,get_start,new_booking_validator,new_order_to_json,get_all_booking,show_by_method_operator,get_by_id,change_booking_operator,canceltaion_operator
from printer import dict_printer,list_printer

def add_new_book():
    name = get_input("enter your name")
    room_id = get_input("room id")
    date = get_date()
    start = get_start()
    players= get_input("enter number of players")
    if not new_booking_validator(name,room_id,date,start,players):
        return
    new_order_to_json(name,room_id,date,start,players)
    return

def print_all_bookings_operator():
    get_all_booking()
    return

def show_book_by_id():
    book_id = get_input("booking id")
    room =get_by_id(book_id)
    if not room:
        return
    dict_printer(room)
    return

def show_by_name():
    name = get_input("name of costumer")
    show_by_method_operator("name",name)
    return

def show_by_date():
    year = int(get_input("year"))
    month = int(get_input("month"))
    day = int(get_input("day"))
    full_date = f"{year}-{month}-{day}"
    res = show_by_method_operator("booking_date",full_date)
    list_printer(res)
    return

def change_booking():
    book_id = get_input("book id")
    book = get_by_id(book_id)
    if not book:
        return
    change_booking_operator(book)
    return

def cancel_booking():
    book_id = get_input("book id")
    book = get_by_id(book_id)
    if not book:
        return
    canceltaion_operator(book["booking_date"],book["start_time"],book_id,book["total_price"])
    return
    

    





if __name__ == "__main__":
    change_booking()

    

    
