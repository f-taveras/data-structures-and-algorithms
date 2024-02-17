class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Append a value to the end of the list."""
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def find(self, matching_function):
        """Find the first node that matches the condition."""
        current = self.head
        while current:
            if matching_function(current.value):
                return current
            current = current.next
        return None

    def remove(self, value):
        """Remove the node with the specified value."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current
            current = current.next
