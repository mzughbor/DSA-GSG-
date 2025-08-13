class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        # Helper to convert linked list to Python list for easier debugging/display
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def is_non_decreasing(self):
        if not self.head or not self.head.next:
            return True # Empty or single-node list is non-decreasing
        current = self.head
        while current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True
    

def solve_list_reduction(linked_list):
    operations = 0
    while not linked_list.is_non_decreasing():
        # Step 1: Find the minimum sum adjacent pair
        min_sum = float('inf')
        min_pair_prev = None # The node *before* the first node of the pair
        min_pair_node1 = None
        min_pair_node2 = None

        current_prev = None
        current = linked_list.head
        while current and current.next:
            current_sum = current.value + current.next.value
            if current_sum < min_sum:
                min_sum = current_sum
                min_pair_prev = current_prev
                min_pair_node1 = current
                min_pair_node2 = current.next
            current_prev = current
            current = current.next

        # If no pair found (e.g., list has only one node left and is not sorted)
        # This case should ideally be covered by is_non_decreasing() earlier.
        if not min_pair_node1 or not min_pair_node2:
            break # No more pairs to reduce, and it's still not non-decreasing

        # Step 2: Replace the two nodes
        new_node = Node(min_sum)

        if min_pair_prev:
            min_pair_prev.next = new_node
        else:
            # The first two nodes were merged, so the new_node becomes the head
            linked_list.head = new_node

        new_node.next = min_pair_node2.next

        operations += 1

    return operations

# Example Usage (from the problem description):
# Input: [5] -> [1] -> [2] -> [3] -> [1] 

ll = LinkedList()
ll.append(5)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(1)

print(f"Initial list: {ll.to_list()}")
result_ops = solve_list_reduction(ll)
print(f"Minimum operations: {result_ops}")
print(f"Final list: {ll.to_list()}")

# 5 3 3 1
# 5 3 4
# 5 7