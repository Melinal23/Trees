"""Given a binary tree and a number, return true if the tree has a root-to-leaf sum such that adding up all the values
 along the sum equals the given number. Return false if no such sum can be found."""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

root = TreeNode(10)
left1 = TreeNode(8)
right1 = TreeNode(2)
left2 = TreeNode(3)
right2 = TreeNode(5)
left3 = TreeNode(2)

root.left = left1
root.right = right1
left1.left = left2
left1.right = right2
right1.left = left3

def root_to_leaf(root, val):

     if not root: #root is none
         return False

     sum = 0

     return helper(root, val, sum)


def helper(root, val, sum):

    found = False

    sum += root.val

    if not root.left and not root.right:
        if sum == val:
            found = True
        else:
            sum -= root.val

    if root.left:
        found |= helper(root.left, val, sum)

    if root.right:
        found |= helper(root.right, val, sum)

    return found

print(root_to_leaf(root, 100))

# same inputs and outputs:
# 21 –> 10 – 8 – 3 -> True
# 23 –> 10 – 8 – 5 -> True
# 14 –> 10 – 2 – 2 -> True