class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BianaryTree:
    def __init__(self, root):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    '''
    def _insert_rec(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data: # this for BST not like normal BT
            node.left = self._insert_rec(node.left, data)
        else:
            node.right = self._insert_rec(node.right, data)
        return node
    '''

    def _insert(self, node, data):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self._insert(node.left, data) # this will make tree unbalanced

    def search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

# Example usage:
bt = BianaryTree(10)
bt.insert(5)
bt.insert(15)
bt.insert(10)
bt.insert(13)
bt.insert(17)
bt.insert(19)
bt.delete(bt.root, 10)
found_node = bt.search(bt.root, 7)
bt.inorder(bt.root)
