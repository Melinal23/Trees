def sumOfLeftLeaves(root):
    return helper(root, child='')


def helper(root, child):
    total = 0

    if not root:
        return 0

    if child == "left" and not root.left and not root.right:
        total += int(root.val)

    if root.left:
        total += helper(root.left, child="left")

    if root.right:
        total += helper(root.right, child="right")

    return total


"""This is someone elses code on leetcode that I thought was a great method"""
def student_helper(self, root):
    if not root: return
    if root.left and root.left.left == None and root.left.right == None:
        self.lVal += root.left.val
    else:
        self.helper(root.left)
    self.helper(root.right)