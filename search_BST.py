class TreeNode:
    def __init__(self, val):
        self. val = val
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

def search_BST(root, val):
    if root is None:
        return False

    if root.val == val:
        return True

    elif root.val > val:
        return search_BST(root.left, val)

    return search_BST(root.right, val)

print(search_BST(root, 18))