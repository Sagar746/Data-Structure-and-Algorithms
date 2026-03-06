class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """

        # YOUR CODE HERE. Remove the next line if necessary
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """

        # YOUR CODE HERE. Remove the next line if necessary
        if not self._top:
            return None
        popped_node = self._top
        self._top = self._top.next
        self._size -= 1
        return popped_node.data

    def __repr__(self):
        # YOUR CODE HERE. Remove the next line if necessary
        elements = []
        current = self._top
        while current:
            elements.append(current.data)
            current = current.next

        return f"<Stack ({self._size} element{'s' if self._size != 1 else ''}): [{', '.join(elements)}]>"


#Test
mystack = Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
print(mystack)