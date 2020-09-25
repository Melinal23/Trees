class TreeNode:
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None

root = TreeNode(5)
left1 = TreeNode(3)
right1 = TreeNode(9)
left2 = TreeNode(7)
right2 = TreeNode(10)

root.left = left1
root.right = right1
right1.left = left2

def print_BFS(root):

    if root == None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        node = queue.pop(0)
        print(node.data)
        if(node.left != None):
            queue.add(node.left)
        if(node.right != None):
            queue.add(node.right)
