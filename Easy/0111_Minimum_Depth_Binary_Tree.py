# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = [(root, 1)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if curr.left == None and curr.right == None:
                    return level
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return 0
        