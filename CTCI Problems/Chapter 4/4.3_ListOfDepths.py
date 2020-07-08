def create_lists_per_level(node, depth, levels=[]):
    if not node:
        return
 
    if depth == 0:
        levels.append(Node(node.value))
    else:
        if depth >= len(levels):
            levels.append(Node(node.value))
        else:
            level = levels[depth]
            while level:
                previous = level
                level = level.next
 
            previous.next = Node(node.value)
 
    create_lists_per_level(node.left, depth+1, levels)
    create_lists_per_level(node.right, depth+1, levels)
 
    return levels
 
 
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
