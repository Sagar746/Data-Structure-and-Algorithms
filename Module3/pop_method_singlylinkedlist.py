class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        # Case 1: empty list
        if not self._head:
            return None

        # Case 2: list has only one node
        if self._head.next is None:
            value = self._head.data
            del self._head
            self._head = None
            return value

        # Case 3: list has more than one node
        current_node = self._head
        # traverse until second-to-last node
        while current_node.next.next is not None:
            current_node = current_node.next

        # current_node is now second-to-last node
        value = current_node.next.data
        del current_node.next
        current_node.next = None
        return value
