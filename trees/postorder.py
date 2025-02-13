class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversalIterative(self, root: TreeNode) -> list[int]:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]

    def postorderTraversalMorris(self, root: TreeNode) -> list[int]:
        result = []
        while root:
            if root.right is None:
                result.append(root.val)
                root = root.left
            else:
                pre = root.right
                while pre.left and pre.left is not root:
                    pre = pre.left
                if pre.left is None:
                    pre.left = root
                    result.append(root.val)
                    root = root.right
                else:
                    pre.left = None
                    root = root.left
        return result[::-1]

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    root.right = TreeNode(8)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(6)
    
    print(Solution().postorderTraversal(root))
    print(Solution().postorderTraversalIterative(root))
    print(Solution().postorderTraversalMorris(root))