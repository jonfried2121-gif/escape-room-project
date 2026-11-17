from menu_printer import room_managment_menu
from input_user import get_input
from python_validations import number_validation
from room_functions import print_all_rooms,print_room_by_id,add_new_room,update_room,update_activity
def room_operator():
    flag = True
    while flag:
        room_managment_menu()
        pick = get_input(" a number")
        if not number_validation(pick):
            continue
        if pick =="1":
            print_all_rooms()
        if pick == "2":
            print_room_by_id()
        if pick =="3":
            add_new_room()
        if pick == "4":
            update_room()
        if pick =="5":
            update_activity()
        if pick == "6":
            flag = False

        else:
            print("please enter a valid number")
            continue
    return

if __name__ == "__main__":
    room_operator()       