# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        stack, sol = [(root, [root.val])], []
        while stack:
            curr, ls = stack.pop()
            if curr.left == curr.right == None and sum(ls) == target:
                sol.append(ls)
            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))
        return sol