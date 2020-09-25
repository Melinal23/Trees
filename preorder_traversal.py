class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(4)
left1 = TreeNode(2)
right1 = TreeNode(6)
left2 = TreeNode(1)
right2 = TreeNode(3)

root.left = left1
root.right = right1
left1.left = left2
left1.right = right2

#       4
#    2     6
#  1   3    ==>  4 2 1 3 6
# prerder traversal is done with DFS
# We want to visit roots before leaves
# We want to visit the left child before the right child.
# root left right


def preorder_traversal_recursive(root):

    if root is None:
        return

    print(root.data)
    preorder_traversal_recursive(root.left)
    preorder_traversal_recursive(root.right)


preorder_traversal_recursive(root)


def preorder_traversal_iterative(root):

    stack = []
    stack.append(root)

    while(len(stack) > 0):  # not empty
        node = stack.pop()
        print(node.data)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)


preorder_traversal_iterative(root)