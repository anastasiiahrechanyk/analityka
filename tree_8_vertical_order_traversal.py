from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root: TreeNode):
    col_table = defaultdict(list)
    queue = deque([(root, 0, 0)])
    while queue:
        node, row, col = queue.popleft()
        if node:
            col_table[col].append((row, node.val))
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))
    res = []
    for col in sorted(col_table.keys()):
        col_table[col].sort()
        res.append([val for row, val in col_table[col]])
    return res

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
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print("Приклад 1:", verticalTraversal(root))

    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("Приклад 2:", verticalTraversal(root))  

    root = build_tree([1, 2, 3, 4, 6, 5, 7])
    print("Приклад 3:", verticalTraversal(root)) 










