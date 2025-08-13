from stackMatieralPractice import  ArrayStack_2 # ArrayStack
from material import ArrayStack

# Create a stack
myStack = ArrayStack(3)

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())
print("Stack: ", myStack.stack)

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.is_empty())

print("Size: ", myStack.is_full())
print("Stack: ", myStack.stack)


print("----------------------------------------------------------------")
#the  fix ?

myStack_02 = ArrayStack_2(2)
myStack_02.push("MAhmoud")
myStack_02.push("Said")
print(">> ", myStack_02.stack)
print("is Full: ", myStack_02.isFull())
print("Pop: ", myStack_02.pop())
print(">> ", myStack_02.stack)
myStack_02.push("Ss")

print("is Empty: ", myStack_02.isEmpty())
print("is Full: ", myStack_02.isFull())
print(">> ", myStack_02.stack)

