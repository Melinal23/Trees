def distance_K(root, target, k):
    if not root:
        return None

    parents = {}
    nodes = []

    find_parents(root, parents)

    # print([(pair[0], pair[1].val) for pair in parents.items()])

    find_nodes(target, nodes, k, parents)

    return nodes


def find_parents(root, parents):
    if not root:
        return

    if root.left and root.left not in parents:
        parents[root.left] = root
        find_parents(root.left, parents)

    if root.right and root.right not in parents:
        parents[root.right] = root
        find_parents(root.right, parents)


def find_nodes(root, nodes, k, parents):
    queue = []

    seen = set()

    queue.append((root, 0))
    seen.add(root)

    while (len(queue) > 0):

        curr = queue.pop(0)

        if curr[1] == k:
            nodes.append(curr[0].val)

        if curr[0].left and curr[0].left not in seen:
            seen.add(curr[0].left)
            queue.append((curr[0].left, curr[1] + 1))

        if curr[0].right and curr[0].right not in seen:
            seen.add(curr[0].right)
            queue.append((curr[0].right, curr[1] + 1))

        if parents.get(curr[0]) and parents.get(curr[0]) not in seen:
            seen.add(parents[curr[0]])
            queue.append((parents[curr[0]], curr[1] + 1))