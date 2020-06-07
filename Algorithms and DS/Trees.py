class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left: self.left.printTree()
        print(self.data)
        if self.right: self.right.printTree()

    def inOrderTraversal(self,root):
        result = []
        if root:
            result = self.inOrderTraversal(root.left)
            result.append(root.data)
            result += self.inOrderTraversal(root.right)
        return result

    def preOrderTraversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.preOrderTraversal(root.left)
            result += self.preOrderTraversal(root.right)
        return result

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inOrderTraversal(root))
print(root.preOrderTraversal(root))