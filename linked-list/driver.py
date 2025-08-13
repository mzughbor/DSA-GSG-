from linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(40)
    linked_list.append(50)

    print("Initial Linked List:")

    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.insert_from_first(5)
    print("\nAfter inserting at the beginning:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.insert_from_middle(30)
    print("\nAfter inserting in the middle:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    linked_list.delete_at_index(3)
    print("\nAfter deleting at index 3:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    
    linked_list.append(100)
    
    print("\nAgain Initial Linked List After Adding 100:")

    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


    middle_node = linked_list.find_middle_node()
    if middle_node:
        print(f"\nThe middle node's data is: {middle_node.data}")
