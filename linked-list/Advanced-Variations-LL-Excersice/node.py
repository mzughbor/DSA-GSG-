class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"