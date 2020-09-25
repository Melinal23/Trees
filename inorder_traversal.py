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
# left3 = TreeNode(6)
# right3 = TreeNode(7)

root.left = left1
root.right = right1
right1.left = left2
right1.right = right2
# right1.left = left3
# right1.right = right3
#       4
#    2     6
#  1   3    ==> 1 2 3 4 6
#inorder traversal is done with DFS

# left root right
def inorder_traversal_recursive(root):

    if root is None:
        return

    inorder_traversal_recursive(root.left)
    print(root.data)
    inorder_traversal_recursive(root.right)


inorder_traversal_recursive(root)

def inorder_traversal_iteratively(root):
    if root is None:
        return
    pass