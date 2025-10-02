# lifo_using_fifo.py

from collections import deque

class StackUsingQueues:
    def __init__(self):
        # Two queues
        self.q1 = deque()  # main queue
        self.q2 = deque()  # helper queue

    def push(self, x):
        """Push element onto stack."""
        # Step 1: enqueue into q2
        self.q2.append(x)

        # Step 2: move all elements from q1 -> q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.q1:
            raise IndexError("pop from empty stack")
        return self.q1.popleft()

    def top(self):
        """Return the top element without removing it."""
        if not self.q1:
            raise IndexError("top from empty stack")
        return self.q1[0]

    def empty(self):
        """Return True if stack is empty."""
        return not self.q1


# -------------------------------
# Test Example
# -------------------------------
if __name__ == "__main__":
    s = StackUsingQueues()

    print("Push: 1, 2, 3")
    s.push(1)
    s.push(2)
    s.push(3)

    print("Top element:", s.top())  # should be 3

    print("Pop:", s.pop())  # should return 3
    print("Pop:", s.pop())  # should return 2

    print("Push: 4")
    s.push(4)

    print("Pop:", s.pop())  # should return 4
    print("Pop:", s.pop())  # should return 1

    print("Is empty?", s.empty())  # should be True
