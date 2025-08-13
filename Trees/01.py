class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):

        def _insert(node, data):
        
            if not node:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            return node

        self.root = _insert(self.root, data)

    def findMin(self):
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.data

    def findMax(self):
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def inorder_traversal(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [node.data] + _inorder(node.right)
        return _inorder(self.root)

# example
bst = BST()
for num in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(num)

print("Inorder traversal:", bst.inorder_traversal())  # [2, 3, 4, 5, 6, 7, 8]
print("Minimum value:", bst.findMin())  # 2
print("Maximum value:", bst.findMax())  # 8
