from collections import deque

"""brute force solution"""

def findSecondMinimumValue(self, root):
    path = []

    self.helper(root, path)

    if len(path) <= 1:
        return -1

    path = sorted(path)

    return path[1]


def helper(self, root, path):
    if not root:
        return

    if root.val not in path:
        path.append(root.val)

    if root.left:
        self.helper(root.left, path)

    if root.right:
        self.helper(root.right, path)


"""optimized solution"""


def findSecondMinimumValue1(self, root):
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

    dfs(root)

    return self.ans if self.ans < float('inf') else -1

"""Solution using BFS"""


def findSecondMinimumValue2(root):
    queue = deque([root])
    res = []
    res.append(root.val)
    while queue:
        node = queue.pop()

        if node.left:
            res.append(node.left.val)
            queue.append(node.left)

        if node.right:
            res.append(node.right.val)
            queue.append(node.right)

    s = sorted(set(res))
    return s[1] if len(s) > 1 else -1