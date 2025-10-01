from .library_item import LibraryItem
from .reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration):
        super().__init__(item_id, title, author)
        self.duration = duration
        self.reserved_by = None

    def display_info(self):
        print(f"DVD: {self.title} directed by {self.author} | Duration: {self.duration} mins | Available: {self.available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("This DVD is already reserved.")
        self.reserved_by = user