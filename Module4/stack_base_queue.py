class Stack:
    def __init__(self):
        self.items = []
        self._size = 0

    def push(self, item):
        self.items.append(item)
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        self._size -= 1
        return self.items.pop()

    def peek(self):
        if self._size == 0:
            return None
        return self.items[-1]

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Stack({self.items})"


class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        # Transfer inbound to outbound if outbound is empty
        if self._OutboundStack._size == 0:
            while self._InboundStack._size > 0:
                self._OutboundStack.push(self._InboundStack.pop())

        self._size -= 1
        return self._OutboundStack.pop()


#Test
queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)