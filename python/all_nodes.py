def all_nodes(root, value):
    if root is None:
        return 0

    if root.val == value:
        return 1 + all_nodes(root.left, value) + all_nodes(root.right, value)
    elif value < root.val:
        return all_nodes(root.left, value)
    else
        return all_nodes(root.right, value)

