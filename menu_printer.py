def main_menu():
    print("""------ESCAPE ROOM SYSTEM------
1. room managment
2. booking managment
3. reports
4. exit""")
    return


def room_managment_menu():
    print("""------ ROOM MANAGMENT------
1. all rooms by name
2. show all rooms details
3. add new room
4. update room
5. update activity
6. back""")
    return

def update_room_menu():
    print("""wehere to update
1.name
2. dificulty
3. duration
4.minimum person
5. maximum person
6. price per person
""")
    return

def booking_managmeny_menu():
    print("""------BOOKING MANAGMENT------
1. new booking
2.show all booking
3. search book by id
4. show bookings by id
5. show bookings by date
6. change excisting book
7. cancell booking
8.exit""")
    return

def change_booking_menu():
    print("""1.date
2.start_hour
3. number of people
4.exit""")
    return


def report_managment_printer():
    print("""------report managment------
1. number of all active bookings
2. number of all cancelled bookings
3. income from active bookings
4. most popular room
5.number of bookings per room
6. percent of capacity ina given room
7.exit""")


