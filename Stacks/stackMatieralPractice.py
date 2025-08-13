# Stack Implementations using Linked List...

##############################################################
# the first LinkedStack will study again laters on... after coming back from LinkedList revision and final study...
# https://www.w3schools.com/dsa/dsa_data_stacks.php

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        to_return = self.top.date
        self.top = self.top.next
        return to_return
    
    def is_empty(self):
        return self.top is None
    
    def clear(self):
        self.top = None

##############################################################

# Stack Implementations using Array... // the simplest way ...

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!"
        return self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty!"
        return self.stack[-1]

##############################################################

# another way of implementation using Arrays // make more sense with C C++ ...

class ArrayStack_2:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.n = -1 # n or top // like the pointer we use to know where we are?!
    
    def isFull(self):
        return self.n == self.capacity-1

    def isEmpty(self):
        return self.n == -1

    def push(self,data):
        if self.isFull():
            print("Stack is Full! Can't add new data.")
            return
        else:
            self.n += 1
            self.stack[self.n] = data
    
    def pop(self):
        if self.isEmpty():
            return None
        value = self.stack[self.n]
        self.stack[self.n] = None
        #self.stack.pop() # use python pop !!
        self.n -= 1
        return value
    
    """ 
    def pop(self):
        if self.isEmpty():
            return None
        else:
            value = self.stack[self.n]
            self.n -= 1
            return value
    """

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.n]
    