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
        to_return = self.top.data
        self.top = self.top.next
        return to_return

    def peek(self):
        return None if self.top is None else self.top.data

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None

def infix_to_postfix(expression):
    """
    should be separated by spaces.
    """
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    output = []
    operator_stack = LinkedStack()

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while (not operator_stack.is_empty() and operator_stack.peek() != '(' and
                   precedence.get(token, 0) <= precedence.get(operator_stack.peek(), 0)):
                output.append(operator_stack.pop())
            operator_stack.push(token)


    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return ' '.join(output)

# Examples
print(f"'(1 + 2) * 3' -> '{infix_to_postfix('( 1 + 2 ) * 3')}'")

print(f"'5 + ( 6 - 2 ) * 9' -> '{infix_to_postfix('5 + ( 6 - 2 ) * 9')}'")

print(f"'( 1 + 2 ) * ( 3 + 4 )' -> '{infix_to_postfix('( 1 + 2 ) * ( 3 + 4 )')}'")


