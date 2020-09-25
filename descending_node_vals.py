"""Given a balanced BST, print out
the integer values in descending order

UMPIRE:

M - similar to in-order but we visit the right node first

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(5)
left1 = TreeNode(3)
right1 = TreeNode(9)
left2 = TreeNode(7)
right2 = TreeNode(10)

root.left = left1
root.right = right1
right1.left = left2
right1.right = right2

def descending_node_values(root):
    pass


