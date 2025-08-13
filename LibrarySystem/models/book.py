from .library_item import LibraryItem
from .reservable import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author)
        self.genre = genre
        self.reserved_by = None

    def display_info(self):
        print(f"Book: {self.title} by {self.author} | Genre: {self.genre} | Available: {self.available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("This book is already reserved.")
        self.reserved_by = user