class TreeNode:
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None

root = TreeNode(10)
left1 = TreeNode(3)
right1 = TreeNode(20)
left2 = TreeNode(7)

root.left = left1
root.right = right1
right1.left = left2

def validate(root):
    if root is None:
        return False
    if root.left == None and root.right == None:
        return True

    return validate_helper(root, 100000, -100000)

def validate_helper(node, max, min):
    if node is None:
        return True

    if(node.data <= min or node.data >= max):
        return False

    return validate_helper(node.left, node.data, min) and validate_helper(node.right,max,node.data)


print(validate(root))

#as we go left, the min. stays the same (root) and
# max becomes the value of the parent node
#as we go right, the min. becomes the parent node
#and max stays the same (root)