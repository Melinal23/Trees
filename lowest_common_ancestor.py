class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

"""LCA of a binary search tree"""
def lca(root, v1, v2):
    if root is None:
        return None

    v1_path = []
    v2_path = []

    lca_helper(root, v1, v1_path)
    lca_helper(root, v2, v2_path)

    if len(v1_path) > len(v2_path):
        while (len(v1_path) > len(v2_path)):
            v1_path.pop()
    elif len(v2_path) > len(v2_path):
        while (len(v2_path) > len(v2_path)):
            v2_path.pop()

    for i in range(len(v1_path) - 1, -1, -1):
        if v1_path[i] == v2_path[i]:
            return Node(v1_path[i])


def lca_helper(root, val, array):

    if root.info > val:
        array.append(root.info)
        return lca_helper(root.left, val, array)
    elif root.info < val:
        array.append(root.info)
        return lca_helper(root.right, val, array)
    else:
        array.append(root.info)
        return

#codepath_soln
def lowest_common_ancestor_soln(root, p, q):
    if root is None:
        return
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root

"""of a binary tree"""


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    v1_path = []
    v2_path = []
    path = ""

    lca_helper(root, p.val, v1_path, path)
    lca_helper(root, q.val, v2_path, path)

    if len(v1_path) > len(v2_path):
        while (len(v1_path) > len(v2_path)):
            v1_path.pop()
    elif len(v2_path) > len(v2_path):
        while (len(v2_path) > len(v2_path)):
            v2_path.pop()

    for i in range(len(v1_path) - 1, -1, -1):
        if int(v1_path[i]) == int(v2_path[i]):
            return Node(int(v1_path[i]))


def lowest_common_ancestor_helper(root, val, paths, path):
    if root and root.val == val:
        path += (str(root.val) + " ")
        paths.extend(path.split())
        return

    if not root.left and not root.right:
        path[:-1]
        return

    if root.left:
        lca_helper(root.left, val, paths, path + str(root.val) + " ")

    if root.right:
        lca_helper(root.right, val, paths, path + str(root.val) + " ")