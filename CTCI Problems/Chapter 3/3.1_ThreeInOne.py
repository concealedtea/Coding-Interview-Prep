class MultiStack:
    def __init__(self,stacksize):
        self.numStacks = 3
        self.array = [0] * (stacksize * self.numStacks)
        self.sizes = [0] * self.numStacks
        self.stackSize = stacksize

    def Push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception('Stack is Full')
        self.sizes[stackNum] += 1
        self.array[self.indexOfTop(stackNum)] = item 
        
    def Pop(self,stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        self.sizes[stackNum] -= 1
        value = self.array[self.indexOfTop(stackNum)]
        self.array[self.indexOfTop(stackNum)] = 0
        return value

    def Peek(self,stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        return self.array[self.indexOfTop(stackNum)]
    
    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0
    
    def isFull(self,stackNum):
        return self.sizes[stackNum] == self.stackSize

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

def ThreeInOne():
    newstack = MultiStack(2)
    print (newstack.isEmpty(1))
    newstack.Push(3, 1)
    print (newstack.Peek(1))
    print (newstack.isEmpty(1))
    newstack.Push(2, 1)
    print (newstack.Peek(1))
    print (newstack.Pop(1))
    print (newstack.Peek(1))
    newstack.Push(3, 1)

ThreeInOne()