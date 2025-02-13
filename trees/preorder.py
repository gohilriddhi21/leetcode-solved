class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversalIterative(self, root: TreeNode) -> list[int]:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def preorderTraversalMorris(self, root: TreeNode) -> list[int]:
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
                    result.append(root.val)
                    root = root.left
                else:
                    pre.right = None
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
    
    print(Solution().preorderTraversal(root))
    print(Solution().preorderTraversalIterative(root))
    print(Solution().preorderTraversalMorris(root))