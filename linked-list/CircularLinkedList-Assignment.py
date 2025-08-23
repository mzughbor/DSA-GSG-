from linked_list import LinkedList
from node import Node

class SortedCircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        
        current = self.head
        
        new_node = Node(value)
        if not current:
            self.head = new_node
            new_node.next = self.head
            return self

        previous = None
        if value < self.head.data:
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return self

        while (current.next != self.head) and (current.next.data < value):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return self


    def print_list(self):
        current = self.head
        if not current:
            print("List is empty")
            return self

        while True:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head Again Circular")        


# Test
if __name__ == "__main__":
    linked_list = SortedCircularLinkedList()
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(3)
    linked_list.insert(9)
    linked_list.insert(1)
    linked_list.insert(4)

    print("full cycle Linked List:")

    linked_list.print_list()
