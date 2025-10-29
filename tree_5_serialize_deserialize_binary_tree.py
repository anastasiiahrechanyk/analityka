class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        res, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        while res and res[-1] == "null":
            res.pop()
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root

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
    codec = Codec()

    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(root)
    print("Приклад 1 серіалізовано:", data)
    restored = codec.deserialize(data)
    print("Приклад 1 десеріалізовано:", tree_to_list(restored))

    root = None
    data = codec.serialize(root)
    print("Приклад 2 серіалізовано:", data)
    restored = codec.deserialize(data)
    print("Приклад 2 десеріалізовано:", tree_to_list(restored))











ChatGPT can make mistakes. Check important info. See Cookie Preferences.
