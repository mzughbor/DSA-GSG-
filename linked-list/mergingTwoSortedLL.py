""" # Merge Two Sorted Linked Lists
# Given two linked lists, write a function to merge them into a new sorted linked list.

from reverseSLL import SLL, Node

# see [img] from https://leetcode.com/problems/merge-two-sorted-lists/

class MergeTwoSortLL(SLL):

    def merge(self, LL1, LL2):
        
        # start from Node holding value 0 / as assumption the question said from 0 to 50 Constraints and sorted use that as key to solve the question.
        
        tail = Node(0)
        
        # temp1 and temp2 movement → drives the while loop exit.
        # tail movement → builds the merged list in the correct order.
        
        temp1 = LL1.head
        temp2 = LL2.head

        while temp1 is not None and temp2 is not None:
            if temp1.data < temp2.data:
                tail.next = temp1
                temp1 = temp1.next # this make our temp1 move forward
            else:
                tail.next = temp2
                temp2 = temp2.next
            tail = tail.next #This is what makes the merged list grow step-by-step.


        # This ensures that if one list still has leftover nodes, 
        # they get appended directly to the merged list. This works because both lists are already sorted.        
        if temp1:
            tail.next = temp1
        if temp2:
            tail.next = temp2
        #self.head = tail.next
        return self

t = MergeTwoSortLL()
t2 = MergeTwoSortLL()
t.add_to_front(6).add_to_front(5).add_to_front(4).retrieve
print("-----")
t2.add_to_front(3).add_to_front(2).add_to_front(1).retrieve
print("-----")
print(t2.merge(t,t2))

"""

# Merge Two Sorted Linked Lists
# Given two linked lists, write a function to merge them into a new sorted linked list.

from reverseSLL import SLL, Node

class MergeTwoSortLL(SLL):

    def merge(self, LL1, LL2):
        # Create a dummy start node (value doesn't matter) to simplify attaching nodes
        temp = Node(0)
        tail = temp  # tail pointer to build the merged list

        temp1 = LL1.head  # pointer for traversing LL1
        temp2 = LL2.head  # pointer for traversing LL2

        while temp1 and temp2:
            if temp1.data < temp2.data:
                tail.next = temp1          # attach LL1 node to merged list
                temp1 = temp1.next         # move forward in LL1
            else:
                tail.next = temp2          # attach LL2 node to merged list
                temp2 = temp2.next         # move forward in LL2

            tail = tail.next               # move forward in the merged list

        # Attach the remaining nodes (only one of these will actually run)
        if temp1:
            tail.next = temp1
        if temp2:
            tail.next = temp2

        # Return the merged list starting from the first real node (skip dummy head)
        self.head = temp.next
        return self

# Example usage
t = MergeTwoSortLL()
t2 = MergeTwoSortLL()
t.add_to_front(6).add_to_front(5).add_to_front(4).retrieve
print("-----")
t2.add_to_front(3).add_to_front(2).add_to_front(1).retrieve
print("-----")
print(t2.merge(t, t2))
