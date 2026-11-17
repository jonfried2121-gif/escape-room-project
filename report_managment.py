from menu_printer import report_managment_printer
from input_user import get_input
from python_validations import number_validation
from report_funcctions import number_all_orders_active,number_of_all_cancelled,all_income,most_popular_room,number_of_bookings_per_room,persent_capacity_by_room,read_json_booking
def report_main():
    flag = True
    while flag:
        report_managment_printer()
        pick = get_input("a nuumber")
        if not number_validation(pick):
            continue

        all_orders = read_json_booking()
        if pick == "1":
            number_all_orders_active(all_orders)
            continue

        if pick == "2":
            number_of_all_cancelled(all_orders)
            continue

        if pick == "3":
            all_income(all_orders)
            continue

        if pick == "4":
            most_popular_room(all_orders)
            continue

        if pick == "5":
            number_of_bookings_per_room(all_orders)
            continue

        if pick == "6":
            room_id = get_input("room id")
            date = get_input("date in Y-M-D format")
            persent_capacity_by_room(room_id,date)
            continue
        if pick == "7":
            flag = False
    return
if __name__ == "__main__":
    report_main()