class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def range_search(root, low, high):
    result = []

    def helper(node):
        if not node:
            return
        # Go left only if needed
        if node.data > low:
            helper(node.left)
        # Add node if in range
        if low <= node.data <= high:
            result.append(node.data)
        # Go right only if needed
        if node.data < high:
            helper(node.right)

    helper(root)
    return result

# Build the test AVL Tree (manually balanced)
root = Node(40)
root.left = Node(20)
root.right = Node(60)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(50)
root.right.right = Node(70)

# Now test it
print("Range 25 to 65:", range_search(root, 25, 65))
# Should return [30, 40, 50, 60]
