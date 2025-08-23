from order import Order

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def list_menu(self):
        index = 1
        for item in self.menu:
            print(f"{index}. {item}")
            index += 1

    def create_order(self, item_indexes):
        order = Order()
        for index in item_indexes:
            if 0 <= index < len(self.menu):
                order.add_item(self.menu[index])
        self.orders.append(order)
        print("Order created and added successfully.")

    def list_orders(self):
        index = 1
        for order in self.orders:
            print(f"Order {index}:\n{order}\n")
            index += 1
