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

def find_node(root, val):
    if root == None:
        return False
    elif (root.data == val):
        return True
    else:
        if(val > root.data):
            return find_node(root.right, val)
        else:
            return find_node(root.left, val)

print(find_node(root, 10))