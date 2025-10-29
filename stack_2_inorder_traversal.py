from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


if __name__ == "__main__":
    # Приклад 1: 
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root))  

    # Приклад 2: 
    print(s.inorderTraversal(None))  

    # Приклад 3: 
    print(s.inorderTraversal(TreeNode(1))) 
