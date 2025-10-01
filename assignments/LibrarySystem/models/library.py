import json
from .book import Book
from .dvd import DVD
from .magazine import Magazine
from .user import User
from .reservable import Reservable
from exceptions.custom_exceptions import *

class Library:
    def __init__(self):
        self.items = []
        self.users = []
        self.items_changed = False
        self.users_changed = False

    def get_next_user_id(self):
        if not self.users:
            return 1
        return max(user.user_id for user in self.users) + 1    

    def load_data(self, item_file="items.json", user_file="users.json"):
        try:
            with open(item_file) as f:
                for item in json.load(f):
                    type_ = item.get("type")
                    item.pop("type", None)
                    if type_ == "Book":
                        self.items.append(Book(**item))
                    elif type_ == "Magazine":
                        self.items.append(Magazine(**item))
                    elif type_ == "DVD":
                        self.items.append(DVD(**item))
            with open(user_file) as f:
                for user in json.load(f):
                    self.users.append(User.from_dict(user))

            print("Items loaded:")
            for i in self.items:
                print(f"  ID: {i.item_id}, Title: {i.title}, Available: {i.available}")

        except Exception as e:
            print("Error loading data:", e)

    def save_data(self, item_file="items.json", user_file="users.json"):
        try:
            if self.items_changed:
                with open(item_file, "w") as f:
                    json.dump([vars(i) for i in self.items], f, indent=2)
                print("Items saved.")
            else:
                print("No changes in items. Skipping save.")

            if self.users_changed:
                with open(user_file, "w") as f:
                    json.dump([vars(u) for u in self.users], f, indent=2)
                print("Users saved.")
            else:
                print("No changes in users. Skipping save.")
        except Exception as e:
            print("Error saving data:", e)
    
    def add_user(self, name, email):
        new_id = self.get_next_user_id()
        user = User(new_id, name, email)
        self.users.append(user)
        self.users_changed = True
        return user
    
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError("User not found.")

    def find_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ItemNotFoundError("Item not found.")