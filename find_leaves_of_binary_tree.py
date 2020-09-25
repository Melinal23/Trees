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


def find_leaves_of_binary_tree(root):

    leaf_nodes = {}

    helper(root, leaf_nodes)

    return leaf_nodes


def helper(root,leaves):

    if not root:
        return -1

    left, right = -1, -1

    if root.left:
        left = helper(root.left, leaves)
    if root.right:
        right = helper(root.right, leaves)

    curr = max(left,right) + 1

    if curr not in leaves:
        leaves[curr] = []

    leaves[curr].append(root.data)

    return curr

print(find_leaves_of_binary_tree(root))



