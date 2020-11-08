class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# inorder: Left, Root, Left
# preorder: Root, Left, Right
# postorder: Left, Right, Root

def construct_BT_from_pre_inorder(preorder, inorder):

    if len(preorder) < 0 or len(inorder) < 0:
        return None

    return helper(preorder, inorder)


def helper(preorder, inorder):

    if len(preorder) == 0 or len(inorder) == 0: # left node
        return

    root = TreeNode(preorder.pop(0))  # init root node

    root_index = 0
    for i in range(len(inorder)):
        if inorder[i] == root.data:
            root_index = i

    root.left = helper(preorder, inorder[:root_index])
    root.right = helper(preorder, inorder[root_index+1:])

    return root

print(construct_BT_from_pre_inorder([1,2,4,8,9,10,11,5,3,6,7], [8,4,10,9,11,2,5,1,6,3,7]))
print(construct_BT_from_pre_inorder([3,9,20,15,7], [9,3,15,20,7]))

