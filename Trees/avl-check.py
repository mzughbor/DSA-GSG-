class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_avl_tree(root):
    
    def check(node):
        if not node:
            return True, 0  # (is_balanced, height)
        
        left_ok, left_height = check(node.left)
        right_ok, right_height = check(node.right)
        
        balance = abs(left_height - right_height)  # balance factor

        is_balanced = left_ok and right_ok and (balance <= 1)
        height = max(left_height, right_height) + 1

        return is_balanced, height

    result, _ = check(root)
    return result
