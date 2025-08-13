# Implement FIFO using LIFO >> 
# Implement the First-In-First-Out (FIFO) concept using only the Last-In-First-Out (LIFO) concept. 
# using array not linked list

class FifoUsingLifo:
    def __init__(self):
        self.inStack = []
        self.outStack = []
    
    def enqueue(self, value):
        self.inStack.append(value)

    def dequeue(self):
        