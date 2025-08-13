from .library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue_number):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine: {self.title} Issue #{self.issue_number} by {self.author} | Available: {self.available}")