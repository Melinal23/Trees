"""Given a binary tree, print all its leaf nodes from left to right"""

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

#       5
#    3     9
#       7     10    ==>  paths: 5,3 and 5,9,7 and 5,9,10
#

def find_all_paths(root):

    array = []

    find_all_paths_helper(root, array)

def find_all_paths_helper(node, array):
    if node is None:
        return

    array.append(str(node.data)) # add to path

    if node.left == None and node.right == None:  # if node is a leaf
        print(" ".join(array))  # print path

    find_all_paths_helper(node.left, array)
    find_all_paths_helper(node.right, array)

    array.pop()

find_all_paths(root)
