class InvalidOperationError(Exception):
    pass

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.is_empty():
            self._front = self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        value = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._back = None
        return value

    @property
    def front(self):
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        return self._front

    def peek(self):
        if self.is_empty():
            return None  # or raise an error if that's the expected behavior
        return self._front.value

    def is_empty(self):
        return self._front is None