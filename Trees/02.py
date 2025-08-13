class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:

    def check_balance_and_height(node: TreeNode) -> int:

        if not node:
            return 0

        left_height = check_balance_and_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_balance_and_height(node.right)
        if right_height == -1:
            return -1

        if (left_height - right_height) > 1:
            return -1 

        return 1 + max(left_height, right_height)

    return check_balance_and_height(root) != -1

# true example
root_balanced = TreeNode(3)
root_balanced.left = TreeNode(9)
root_balanced.right = TreeNode(20)
root_balanced.right.left = TreeNode(15)
root_balanced.right.right = TreeNode(7)

print(f"Is the tree balanced? {isBalanced(root_balanced)}")

# false example
root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.right = TreeNode(2)
root_unbalanced.left.left = TreeNode(3)
root_unbalanced.left.right = TreeNode(3)
root_unbalanced.left.left.left = TreeNode(4)

print(f"Is the tree balanced? {isBalanced(root_unbalanced)}")
