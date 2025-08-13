# circular_linked_list.py

from node import Node

class CircularLinkedList:
    """
    Implements a circular singly linked list.
    The last node's 'next' pointer points back to the head.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Points to itself for a single-node circular list
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Maintain circularity
        self.size += 1

    def remove(self, data):
        """
        Removes the first occurrence of a node with the given data.
        Returns True if removed, False otherwise.
        """
        if self.is_empty():
            return False

        current = self.head
        previous = None

        # Handle the case where the head needs to be removed
        if current.data == data:
            if self.head == self.tail: # Only one node in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head # Maintain circularity
            self.size -= 1
            return True

        # Traverse to find the node to remove
        while current != self.tail and current.data != data:
            previous = current
            current = current.next

        # If the node is found (not the head, handled above)
        if current.data == data:
            previous.next = current.next
            if current == self.tail: # If removing the tail
                self.tail = previous
            self.size -= 1
            return True
        
        return False # Data not found

    def get_node_at_index(self, index):
        """
        Returns the node at the specified index.
        Assumes the list is not empty and index is valid.
        """
        if self.is_empty():
            raise IndexError("List is empty")
        if not (0 <= index < self.size):
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def display(self):
        """Prints the elements of the circular linked list."""
        if self.is_empty():
            print("Circular Linked List: Empty")
            return

        elements = []
        current = self.head
        # Traverse until we loop back to the head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print("Circular Linked List:", " -> ".join(map(str, elements)))

    def find_node(self, data):
        """
        Finds and returns the node containing the given data.
        Returns None if not found.
        """
        if self.is_empty():
            return None
        
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head: # looped back
                break
        return None