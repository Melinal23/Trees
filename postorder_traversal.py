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
#  1   3    ==>  1 3 2 6 4

#postorder traversal is done with DFS

# left right root
def postorder_traversal_recursive(root):

    if root is None:
        return


    postorder_traversal_recursive(root.left)
    postorder_traversal_recursive(root.right)
    print(root.data)

# postorder_traversal_recursive(root)

def postorder_list(array, node_indx):
    if (node_indx >= len(array) or array[node_indx] == None):
        return

    postorder_list(array, node_indx*2 + 1) #left
    postorder_list(array, node_indx*2 + 2) #right
    print(array[node_indx])

""" 4
  2   6
1  3  5  7"""

array = [4, 2, 6, 1, 3, 5, 7]

# postorder_list(array, 0)


def postorder_traversal_iteratively(root):
    if root is None:
        return

    stack = []

    while(True):

        while(root):
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        top = None
        if(len(stack) > 0):
            top = stack[-1]

        if(root.right is not None and root.right == top):
            stack.pop() #right child
            stack.append(root)
            root = root.right
        else:
            print(root.data)
            root = None

        if(len(stack) <= 0):
            break


postorder_traversal_iteratively(root)

def postorder_traversal_iteratively_2(root):
    pass