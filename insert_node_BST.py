class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)

    elif root.val > val:  # insert left
        root.left = insertIntoBST(root.left, val)

    elif root.val < val:  # insert right
        root.right = insertIntoBST(root.right, val)

    return root