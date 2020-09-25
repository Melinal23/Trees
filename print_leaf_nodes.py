"""Given a binary tree, print all its leaf nodes from left to right"""

class TreeNode:
    def __init__(self, data):
        self. data = data
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

#       5
#    3     9
#       7     10    ==>  3, 7, 10
#
def print_leafs(root):

    if root is None:
        return
    if root.left == None and root.right == None:
        print(root.data)

    print_leafs(root.left)
    print_leafs(root.right)

print_leafs(root)
