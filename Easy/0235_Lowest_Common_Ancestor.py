# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, p, q):
        if node.val > p and node.val > q:
            return self.traverse(node.left, p, q)
        if node.val < p and node.val < q:
            return self.traverse(node.right, p, q)
        return node
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.traverse(root, p.val, q.val)
    