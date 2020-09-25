class TreeNode:
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None

root = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(3)
# left2 = TreeNode(7)
# right2 = TreeNode(10)

root.left = left1
root.right = right1
# right1.left = left2


def invert_BST(root):
    if root is None:
        return

    temp = root.right      #flip the child nodes
    root.right = root.left
    root.left = temp

    invert_BST(root.right)
    invert_BST(root.left)

    return root