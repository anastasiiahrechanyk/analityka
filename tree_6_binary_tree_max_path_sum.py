class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float("-inf")

    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)

    helper(root)
    return max_sum

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
    root = build_tree([1, 2, 3])
    print("Приклад 1:", maxPathSum(root))  

    root = build_tree([-10, 9, 20, None, None, 15, 7])
    print("Приклад 2:", maxPathSum(root)) 










