# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maximum = None
    def recursive(self, node):
        if not node: return 0
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        result = left + right + node.val
        self.maximum = max(result, self.maximum)
        return max(right + node.val, left + node.val, node.val, 0)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recursive(root)
        return self.maximum