class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root: TreeNode) -> int:
    cameras = 0

    def dfs(node):
        nonlocal cameras
        if not node:
            return 1
        left = dfs(node.left)
        right = dfs(node.right)
        if left == 0 or right == 0:
            cameras += 1
            return 2
        if left == 2 or right == 2:
            return 1
        return 0

    if dfs(root) == 0:
        cameras += 1
    return cameras

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
    root = build_tree([0, 0, None, 0, 0])
    print("Приклад 1:", minCameraCover(root)) 

    root = build_tree([0, 0, None, 0, None, 0, None, None, 0])
    print("Приклад 2:", minCameraCover(root))  











ChatGPT can make mistakes. Check important info. See Cookie Preferences.
