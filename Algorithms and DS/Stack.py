class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

s = Stack()
print(s.isEmpty())
s.push(3)
s.push(4)
print(s.isEmpty())
print(s.peek())
s.pop()
print(s.peek())
print(s.size())