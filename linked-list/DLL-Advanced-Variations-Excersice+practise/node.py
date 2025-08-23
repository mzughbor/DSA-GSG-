class Node:
    """
    Represents a node in a linked list.
    head and tail related to the DLL class not to the node itself, so only data and next is important.//and maybe previous
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"