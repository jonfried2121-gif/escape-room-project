from python_validations import number_validation
from input_user import get_input
from menu_printer import booking_managmeny_menu
from booking_functions import add_new_book,print_all_bookings_operator,show_book_by_id,show_by_name,show_by_date,change_booking,cancel_booking

def booking_managment_operator():
    
    flag = True
    booking_managmeny_menu()
    while flag:
        pick = get_input("a pick")
        if not number_validation(pick):
            return
        if pick == "1":
            add_new_book()
            continue
        if pick == "2":
            print_all_bookings_operator()
            continue
        if pick == "3":
            show_book_by_id()
            continue
        if pick == "4":
            show_by_name()
            continue
        if pick == "5":
            show_by_date()
            continue
        if pick == "6":
            change_booking()
            continue
        if pick == "7":
            cancel_booking()
            continue
        if pick == "8":
            flag = False
    return


        