
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self._insert(node.left, data) # left first inseration 
    
    def search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self.search(node.left, target) or self.search(node.right, target)
    
    