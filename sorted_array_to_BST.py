class TreeNode:
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None

    return insert(nums, 0, len(nums) - 1)


def insert(nums, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = TreeNode(nums[mid])
    root.left = insert(nums, start, mid - 1)
    root.right = insert(nums, mid + 1, end)

    return root