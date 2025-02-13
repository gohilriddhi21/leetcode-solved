class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    def inorderTraversalIterative(self, root: TreeNode) -> list[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def inorderTraversalMorris(self, root: TreeNode) -> list[int]:
        result = []
        while root:
            if root.left is None:
                result.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    result.append(root.val)
                    root = root.right
        return result

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    root.right = TreeNode(8)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(6)
    
    print(Solution().inorderTraversal(root))
    print(Solution().inorderTraversalIterative(root))
    print(Solution().inorderTraversalMorris(root))