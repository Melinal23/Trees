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

#the input tree is a BST, not necessary balanced
def second_largest_node(root):

    if(root.right is None and root.left is None):
        return root.data

    if(root.left is not None and root.right is None):
        return second_largest_node(root.left)

    if root.right is not None \
            and root.right.right is None \
            and root.right.left is None:
        return root.data

    return second_largest_node(root.right)

print(second_largest_node(root))