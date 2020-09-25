class TreeNode:
    def __init__(self, data):
        self. data = data
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
#  1   3    ==>  4 2 6 1 3
#Levelorder traversal is done with BFS


def levelorder_traversal(root):

    q = []
    q.append(root)

    while(len(q) > 0):  # not empty
        node = q.pop(0)
        print(node.data)
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)


levelorder_traversal(root)