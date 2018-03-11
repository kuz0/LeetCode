# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        h = abs(self.getHeight(root.left)-self.getHeight(root.right))
        if h > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    result = Solution().isBalanced(root)
    print(result)

    root.left.left = TreeNode(2)
    result = Solution().isBalanced(root)
    print(result)
