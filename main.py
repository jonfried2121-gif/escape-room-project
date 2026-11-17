from menu_printer import main_menu
from input_user import get_input
from python_validations import number_validation
from room_managment import room_operator
from booking_managment import booking_managment_operator
from report_managment import report_main
def menu():
    flag  = True
    main_menu()
    while flag:
        pick = get_input(" a number")
        if not number_validation(pick):
            continue
        if pick == "1":
            room_operator()
            continue

        if pick =="2":
            booking_managment_operator()
            continue

        if pick == "3":
            report_main()
            continue

        if pick == "4":
            flag = False

        else:
            print("please pick a valid number")
            continue

menu()


