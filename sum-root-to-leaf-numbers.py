"""Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers."""


def sumNumbers(root):
    if root is None:
        return 0

    paths = []

    sumNumbersHelper(root, paths, path="")

    return sum(int(num) for num in paths)


def sumNumbersHelper(root, paths, path):
    if root:
        path += str(root.val)

    if root.left is None and root.right is None:
        paths.append(path)
        path = path[:-1]
        return  # optional

    if root.left is not None:
        sumNumbersHelper(root.left, paths, path)

    if root.right is not None:
        sumNumbersHelper(root.right, paths, path)

