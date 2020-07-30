# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                try:
                    if level % 2 == 0:
                        ans[level].append(curr.val)
                    else:
                        ans[level] = [curr.val] + ans[level]
                except IndexError:
                    ans.append([curr.val])
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return ans
            
        