class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal: str) -> TreeNode:
    stack = []
    i = 0
    while i < len(traversal):
        depth = 0
        while i < len(traversal) and traversal[i] == '-':
            depth += 1
            i += 1
        val_start = i
        while i < len(traversal) and traversal[i].isdigit():
            i += 1
        val = int(traversal[val_start:i])
        node = TreeNode(val)
        while len(stack) > depth:
            stack.pop()
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
    return stack[0]

def tree_to_list(root):
    if not root:
        return []
    res, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == "__main__":
    traversal = "1-2--3--4-5--6--7"
    root = recoverFromPreorder(traversal)
    print("Приклад 1:", tree_to_list(root))  

    traversal = "1-2--3---4-5--6---7"
    root = recoverFromPreorder(traversal)
    print("Приклад 2:", tree_to_list(root))  

    traversal = "1-401--349---90--88"
    root = recoverFromPreorder(traversal)
    print("Приклад 3:", tree_to_list(root)) 











ChatGPT can make mistakes. Check important info. See Cookie Preferences.
