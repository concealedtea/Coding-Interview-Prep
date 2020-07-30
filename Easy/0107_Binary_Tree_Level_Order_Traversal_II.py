# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                try: ans[level].append(curr.val)
                except IndexError: ans.append([curr.val])
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return ans[::-1]