class Queue:
    def __init__(self):
        self._size = 0
        self._head = None  # newest (left)
        self._tail = None  # oldest (right)

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []
        current = self._head
        while current:
            values.append(str(current.data))
            current = current.next
        return f'<Queue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        new_node = ListNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None
        data = self._tail.data
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return data

#Test
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

q = Queue()
print(q)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q)
print(q.dequeue())
print(q)