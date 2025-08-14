from linked_list import LinkedList
from remove_Duplicates import RemoveDuplicates

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append_to_end(10)
    linked_list.append_to_end(20)
    linked_list.append_to_end(40)
    linked_list.append_to_end(50)

    print("Initial Linked List:")

    linked_list.retrieve

    linked_list.insert_from_first(5)
    print("\nAfter inserting at the beginning:")
    linked_list.retrieve

    # for testing the remover duplicates
    linked_list.insert_from_first(5)
    print("\nAfter inserting at the beginning:")
    linked_list.retrieve

    linked_list.insert_from_middle(30)
    print("\nAfter inserting in the middle:")
    linked_list.retrieve

    linked_list.delete_at_index(3)
    print("\nAfter deleting at index 3:")
    linked_list.retrieve

    middle_node = linked_list.find_middle_node()
    if middle_node:
        print(f"\nThe middle node's data is: {middle_node.data}")

    #test duplicater removen
    RemoveDuplicates.RemoveDuplicate(linked_list)
    linked_list.retrieve

    # anotehr test case
    m = LinkedList()
    m.append_to_end(1)
    m.append_to_end(2)
    m.append_to_end(3)
    m.append_to_end(3)
    m.append_to_end(4)
    m.append_to_end(4)
    m.append_to_end(5)
    m.append_to_end(6)
    m.append_to_end(7)
    m.append_to_end(7)

    print("anotehr test case")
    m.retrieve    
    RemoveDuplicates.RemoveDuplicate(m)
    m.retrieve
