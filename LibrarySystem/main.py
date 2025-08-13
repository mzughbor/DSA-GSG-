from models.library import Library
from models.reservable import Reservable
from exceptions.custom_exceptions import *

lib = Library()
lib.load_data()

def show_menu():
    print("\nWelcome to the Library System")
    print("1. View all available items")
    print("2. Register as a new user")
    print("3. Borrow an item")
    print("4. Reserve an item")
    print("5. Return an item")
    print("6. Exit and Save")

while True:
    show_menu()
    try:
        choice = int(input("Choose an option: "))
        if choice == 1:
            for item in lib.items:
                item.display_info()

        elif choice == 2:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            user = lib.add_user(name, email)

            lib.users_changed = True
            print("User registered with ID:", user.user_id)

        elif choice == 3:
            uid = int(input("Enter your user ID: "))
            iid = int(input("Enter item ID: "))
            user = lib.find_user(uid)
            item = lib.find_item(iid)
            if not item.available:
                raise ItemNotAvailableError("Item not available.")
            item.available = False
            user.borrowed_items.append(iid)
            lib.items_changed = True
            lib.users_changed = True
            print("Item borrowed successfully.")

        elif choice == 4:
            uid = int(input("Enter your user ID: "))
            iid = int(input("Enter item ID: "))
            user = lib.find_user(uid)
            item = lib.find_item(iid)
            if isinstance(item, Reservable):
                item.reserve(user)
                lib.items_changed = True
                print("Item reserved.")
            else:
                print("This item cannot be reserved.")

        elif choice == 5:
            uid = int(input("Enter your user ID: "))
            iid = int(input("Enter item ID to return: "))
            user = lib.find_user(uid)
            item = lib.find_item(iid)
            if iid in user.borrowed_items:
                user.borrowed_items.remove(iid)
                item.available = True
                lib.items_changed = True
                lib.users_changed = True
                print("Item returned.")
            else:
                print("This item was not borrowed.")

        elif choice == 6:
            if lib.users_changed:
                lib.save_data()
                #lib.add_users()
            if lib.items_changed:
                lib.save_items()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

    except Exception as e:
        print("Error:", e)