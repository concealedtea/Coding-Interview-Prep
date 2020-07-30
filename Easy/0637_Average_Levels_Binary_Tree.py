# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        bfs, queue = [], [(root, 0)]
        ans = []
        while queue:
            curr, level = queue.pop(0)
            if curr:
                try:
                    bfs[level].append(curr.val)
                except IndexError:
                    bfs.append([curr.val])
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
            ans.append(sum(bfs[-1]) / len(bfs[-1]))
        res = [0] * len(bfs)
        for level, nodes in enumerate(bfs):
            res[level] = sum(nodes) * 1.0 / len(nodes)
        return res