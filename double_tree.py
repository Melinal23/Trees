"""For each node in a binary tree, create
a new duplicate node, and insert the duplicate
as the left child of the original node."""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def doubleTree(root) :

    if root is None:
        return None

    nodes = []
    get_nodes(root, nodes)

    for val in nodes:
        insert(val, root)

    return root

def get_nodes(root, array):  #preorder traversal
    if root is None:
        return

    array.append(root.val)
    get_nodes(root.left, array)
    get_nodes(root.right, array)

def insert(val, root):
    if root is None:
        return

    if val == root.val:
        newNode = TreeNode(val)
        temp = root.left
        root.left = newNode
        newNode.left = temp
        return

    insert(val, root.left)
    insert(val, root.right)