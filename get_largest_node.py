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

#assuming input is BST
def get_largest_node(root):

    if(root.right is not None):
        return get_largest_node(root.right)

    return root.data

print(get_largest_node(root))