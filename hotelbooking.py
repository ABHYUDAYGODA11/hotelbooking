rooms = {}

def addroom(room_number, guest_name):
    rooms[room_number] = guest_name
    print(f"Room {room_number} has been reserved for {guest_name}.")

def removeroom(room_number):
    if room_number in rooms:
        guest_name = rooms.pop(room_number)
        print(f"Room {room_number} has been checked out by {guest_name}.")
    else:
        print(f"Room {room_number} is not currently reserved.")

def displayrooms():
    print("Current Reservations:")
    for room, guest in rooms.items():
        print(f"Room {room}: {guest}")

while True:
    print("Welcome To Hotel Management System")
    print("1. Add a room")
    print("2. Remove a room")
    print("3. Display all rooms")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        room_number = int(input("Enter room number: "))
        guest_name = input("Enter guest name: ")
        addroom(room_number, guest_name)

    elif choice == "2":
        room_number = int(input("Enter room number: "))
        removeroom(room_number)

    elif choice == "3":
        displayrooms()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
