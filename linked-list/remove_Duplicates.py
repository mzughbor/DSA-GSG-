# Exercise 3: Remove Duplicates
#   Given a linked list with duplicates, remove all duplicate entries.
#   Assume input list is sorted.

from linked_list import LinkedList

class RemoveDuplicates(LinkedList):
    
    def RemoveDuplicate(self):
        temp = self.head
        while temp.next: # following the sorted list so it's ok to only check the next elemnt and you ready to go
            if temp.data == temp.next.data:
                print(temp.data)
                if not temp.next.next:
                    temp.next = temp.next.next
                    # that if means you reach the last elemnt stop
                    break
                else:
                    temp.next = temp.next.next
            temp = temp.next

        return self