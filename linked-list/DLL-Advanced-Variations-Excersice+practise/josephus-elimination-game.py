# josephus_solver.py

from circularLinkedList import CircularLinkedList

def solve_josephus_circular_ll(n, k):

    if n <= 0:
        raise ValueError("Number of people (n) must be positive.")
    if k <= 0:
        raise ValueError("Elimination step (k) must be positive.")

    ll = CircularLinkedList()
    for i in range(1, n + 1):
        ll.append(i) # Add people with identifiers 1 to n

    # If only one person, they are the survivor
    if ll.size == 1:
        return ll.head.data

    current = ll.head # Start counting from the first person

    while ll.size > 1:
        # Move k-1 steps to find the person to eliminate
        # The current node is the starting point (step 1), so we need k-1 more steps
        for _ in range(k - 1):
            current = current.next
        
        # 'current' is now the node to be eliminated
        person_to_eliminate = current.data
        
        # Find the previous node to properly remove from the linked list
        # This is the most complex part with a singly linked list
        # A doubly circular linked list would make this easier.
        previous = current
        while previous.next != current:
            previous = previous.next
        
        # Perform removal
        if current == ll.head:
            ll.head = current.next
            ll.tail.next = ll.head # Update tail's next to new head
        elif current == ll.tail:
            ll.tail = previous
            ll.tail.next = ll.head # Update new tail's next to head
        else:
            previous.next = current.next
        
        # Update the size after removal
        ll.size -= 1
        
        # Move 'current' to the next person in the circle for the next round
        current = current.next
        
        # print(f"Eliminated: {person_to_eliminate}. Remaining size: {ll.size}")
        # ll.display() # Uncomment to see steps

    return ll.head.data # The last remaining person


# main.py
if __name__ == "__main__":
    print("--- Josephus Elimination Game using Circular Linked List ---")

    # Example 1: From the problem description (n=5, k=3)
    n1 = 5
    k1 = 3
    print(f"\nSolving for n={n1}, k={k1}...")
    result1 = solve_josephus_circular_ll(n1, k1)
    print(f"The last remaining person for n={n1}, k={k1} is: {result1}") # Expected: 4

    # Example 2: Another common example (n=7, k=3)
    n2 = 7
    k2 = 3
    print(f"\nSolving for n={n2}, k={k2}...")
    result2 = solve_josephus_circular_ll(n2, k2)
    print(f"The last remaining person for n={n2}, k={k2} is: {result2}") # Expected: 4

    # Example 3: (n=10, k=2)
    n3 = 10
    k3 = 2
    print(f"\nSolving for n={n3}, k={k3}...")
    result3 = solve_josephus_circular_ll(n3, k3)
    print(f"The last remaining person for n={n3}, k={k3} is: {result3}") # Expected: 5
    
    # Example 4: Single person
    n4 = 1
    k4 = 5
    print(f"\nSolving for n={n4}, k={k4}...")
    result4 = solve_josephus_circular_ll(n4, k4)
    print(f"The last remaining person for n={n4}, k={k4} is: {result4}") # Expected: 1