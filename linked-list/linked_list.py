from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_from_first(self, value):
        """Inserts a new node at the beginning of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_from_middle(self, value):
        """Inserts a new node at the middle of the linked list."""
        if not self.head:
            self.head = Node(value)
            return

        slow = self.head
        fast = self.head
        previous = None

        while fast and fast.next:
            fast = fast.next.next
            previous = slow
            slow = slow.next

        new_node = Node(value)
        if previous:  # List has at least two nodes
            new_node.next = slow
            previous.next = new_node
        else:  # List has only one node
            new_node.next = self.head
            self.head = new_node

    def delete_at_index(self, index):
        """Deletes the node at the specified index (0-based)."""
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        count = 0

        while current:
            if count == index:
                if previous:
                    previous.next = current.next
                return
            previous = current
            current = current.next
            count += 1
                
    def find_middle_node(self):
        
        head = self.head
        if head is None:
            return None

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    @property
    def retrieve(self):
        current = self.head
        while current != None:
            print(current.data, end="-> ")
            current = current.next
        print("None", end="")
        print("\n")
        return self
        