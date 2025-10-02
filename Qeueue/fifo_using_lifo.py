# fifo_using_lifo.py

class QueueUsingStacks:
    def __init__(self):
        # Two stacks
        self.stack_in = []   # used for enqueue
        self.stack_out = []  # used for dequeue

    def enqueue(self, x):
        """Push element into the queue."""
        self.stack_in.append(x)

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        self._move_in_to_out()
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        return self.stack_out.pop()

    def peek(self):
        """Return the element at the front without removing it."""
        self._move_in_to_out()
        if not self.stack_out:
            raise IndexError("peek from empty queue")
        return self.stack_out[-1]

    def empty(self):
        """Return True if the queue is empty."""
        return not self.stack_in and not self.stack_out

    def _move_in_to_out(self):
        """Move elements from stack_in to stack_out if needed."""
        if not self.stack_out:  # only move if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# -------------------------------
# Test Example
# -------------------------------
if __name__ == "__main__":
    q = QueueUsingStacks()

    print("Enqueue: 1, 2, 3")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Peek front:", q.peek())   # should be 1

    print("Dequeue:", q.dequeue())  # should return 1
    print("Dequeue:", q.dequeue())  # should return 2

    print("Enqueue: 4")
    q.enqueue(4)

    print("Dequeue:", q.dequeue())  # should return 3
    print("Dequeue:", q.dequeue())  # should return 4

    print("Is empty?", q.empty())   # should be True
