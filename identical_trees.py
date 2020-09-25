class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSameTree(self, p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)