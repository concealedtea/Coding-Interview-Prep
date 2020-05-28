import sys
class MultiStack:
    def __init__(self,stacksize):
        self.numStacks = 3
        self.array = [0] * (stacksize * self.numStacks)
        self.sizes = [0] * self.numStacks
        self.stackSize = stacksize
        self.stackMin = [sys.maxsize] * (stacksize * self.numStacks)

    def Push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception('Stack is Full')
        if self.isEmpty(stackNum):
            self.stackMin[self.indexOfTop(stackNum)] = item
        self.sizes[stackNum] += 1
        self.array[self.indexOfTop(stackNum)] = item 
        self.stackMin[self.indexOfTop(stackNum)] = min(item, self.stackMin[self.indexOfTop(stackNum) - 1])
        
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

    def Min(self, stackNum):
        return self.stackMin[self.indexOfTop(stackNum)]
    
    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0
    
    def isFull(self,stackNum):
        return self.sizes[stackNum] == self.stackSize

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

def StackMin():
    newstack = MultiStack(10)
    newstack.Push(5, 0)
    newstack.Push(6, 0)
    newstack.Push(2, 0)
    newstack.Push(7, 0)
    newstack.Push(14, 0)
    newstack.Push(3, 0)
    print (newstack.Min(0))
    newstack.Push(1, 0)
    newstack.Push(4, 0)
    newstack.Push(44, 0)
    newstack.Push(2, 0)
    print (newstack.Min(0))
    newstack2 = MultiStack(10)
    newstack2.Push(2,0)
    newstack2.Push(1,0)
    newstack2.Pop(0)
    print(newstack2.Min(0))

StackMin()