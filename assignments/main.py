from menu_items import MenuItem
from restaurant import Restaurant

def main():
    restaurant = Restaurant()

    while True:
        print("\nWelcome to the Restaurant Management System!")
        print("Choose an option:")
        print("1. Add menu item")
        print("2. View menu")
        print("3. Create new order")
        print("4. List all orders")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue
            category = input("Enter item category: ")
            item = MenuItem(name, price, category)
            restaurant.add_menu_item(item)
            print("Menu item added successfully.")

        elif choice == "2":
            print("Menu:")
            restaurant.list_menu()

        elif choice == "3":
            restaurant.list_menu()
            indexes = input("Enter item numbers for the order separated by commas (e.g., 1,2): ")

            item_indexes = []
            for i in indexes.split(","):
                i = i.strip()
                if i.isdigit():
                    item_indexes.append(int(i) - 1)

            restaurant.create_order(item_indexes)

        elif choice == "4":
            print("Orders:")
            restaurant.list_orders()

        elif choice == "5":
            print("Thank you for using the Restaurant Management System!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
