class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def printBTree(bTree):
    q = [bTree]
    while q:
        curr = q.pop(0)
        print(curr.value)
        if curr != None:
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
    return

def convertToBinary(arr, start, end):
    if start > end: return ''
    mid = (start + end) // 2 # Finds floor mid point
    root = TreeNode(arr[mid])
    root.left = convertToBinary(arr, start, mid - 1)
    root.right = convertToBinary(arr, mid + 1, end)
    return root

arr = [1,2,3,4,5,6,7]
bTreeRoot = convertToBinary(arr, 0, len(arr) - 1)
print(checkBalanced(bTreeRoot))
arr = [1,2,3,4,5,6,7,100,300,400,500,600,700]
bTreeRoot = convertToBinary(arr, 0, len(arr) - 1)
printBTree(bTreeRoot)