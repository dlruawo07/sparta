def make_lst_by(root):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst