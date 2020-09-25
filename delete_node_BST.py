class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delete(root, key):
    if root is None:
        return None

    if root.data == key:
        #node is a leaf
        if root.left is None and root.right is None:
            return None

        #node has 1 child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        #node has 2 children
        min_val = get_inorder_successor(root.right)
        root.data = min_val
        root.right = delete(root.right, min_val)

    elif root.data > key:
        root.left = delete(root.left, key)

    else:
        root.right = delete(root.right, key)

    return root

def get_inorder_successor(root):
    while(root.left != None):
        root = root.left

    return root.val