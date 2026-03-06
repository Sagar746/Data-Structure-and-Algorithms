class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def check_balance(text):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    opens = set('([{')
    closes = set(')]}')
    count = 0
    size = 0

    for i, ch in enumerate(text):
        if ch in opens:
            stack.push((ch, i))
            size += 1
        elif ch in closes:
            if size == 0:
                return f"Match error at position {i}"
            top, _ = stack.pop()
            size -= 1
            if top != pairs[ch]:
                return f"Match error at position {i}"
            count += 1

    if size > 0:
        _, pos = stack.pop()
        return f"Match error at position {pos}"

    return f"Ok - {count}"

#Tests
print(check_balance("a(b)c[d]e{f}g"))
print(check_balance("a(b]c"))
print(check_balance("]abc"))
print(check_balance("(abc"))