# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "null,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)
    
    def deserializeQ(self, q):
        if not q: return None
        val = q.popleft()
        if val == 'null': return None
        node = TreeNode(val)
        node.left = self.deserializeQ(q)
        node.right = self.deserializeQ(q)
        return node

    def deserialize (self, data):
        q = collections.deque(data.split(','))
        return self.deserializeQ(q)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))