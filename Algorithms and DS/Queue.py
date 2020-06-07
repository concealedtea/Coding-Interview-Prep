class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)

s = Queue()
print(s.isEmpty())
s.push(3)
s.push(4)
print(s.isEmpty())
print(s.peek())
s.pop()
print(s.peek())
print(s.size())