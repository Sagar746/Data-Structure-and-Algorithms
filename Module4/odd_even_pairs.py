def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:  # even
            if odd_queue._size > 0:
                odd = odd_queue.dequeue()
                pairs.append((num, odd))
            else:
                even_queue.enqueue(num)
        else:  # odd
            if even_queue._size > 0:
                even = even_queue.dequeue()
                pairs.append((even, num))
            else:
                odd_queue.enqueue(num)

    return pairs

#Test
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

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


print(get_pairs([1, 2, 3, 4, 5, 6]))
print(get_pairs([2, 4, 1, 3]))
print(get_pairs([1, 3, 5, 2]))
print(get_pairs([]))