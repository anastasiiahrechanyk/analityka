class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    print("Приклад 1:", isSameTree(p, q))  # True

    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    print("Приклад 2:", isSameTree(p, q))  # False

    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    print("Приклад 3:", isSameTree(p, q))  # False






