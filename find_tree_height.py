class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(4)
left1 = TreeNode(2)
right1 = TreeNode(6)
left2 = TreeNode(1)
right2 = TreeNode(3)

root.left = left1
root.right = right1
left1.left = left2
left1.right = right2

def find_tree_height(root):
    if root is None:
        return -1

    left = find_tree_height(root.left)
    right = find_tree_height(root.right)

    return max(left,right) + 1

print(find_tree_height(root))