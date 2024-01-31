class Stack:
    """
    A simple implementation of a stack data structure using a Python list.

    Methods:
    push(item): Adds an item to the top of the stack.
    pop(): Removes and returns the top item from the stack. Raises IndexError if the stack is empty.
    is_empty(): Checks if the stack is empty. Returns True if empty, False otherwise.
    peek(): Returns the top item from the stack without removing it. Raises IndexError if the stack is empty.
    """

    def __init__(self):
        """
        Initializes a new empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
        item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Returns:
        The top item from the stack.

        Raises:
        IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Returns:
        The top item of the stack.

        Raises:
        IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")


class PseudoQueue:
    """
    A queue implementation using two stacks. This class simulates a queue's behavior (FIFO)
    using the LIFO principle of stacks.

    Methods:
    enqueue(value): Adds a value to the end of the queue.
    dequeue(): Removes and returns the front value from the queue.
    """

    def __init__(self):
        """
        Initializes the PseudoQueue with two empty stacks.
        """
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        """
        Adds a value to the end of the PseudoQueue.

        Args:
        value: The value to be added to the queue.
        """
        # Move all elements from dequeue_stack to enqueue_stack
        while not self.dequeue_stack.is_empty():
            self.enqueue_stack.push(self.dequeue_stack.pop())

        # Push item into enqueue_stack
        self.enqueue_stack.push(value)

    def dequeue(self):
        """
        Removes and returns the front value from the PseudoQueue.

        Returns:
        The front value of the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        # Move all elements back to dequeue_stack
        while not self.enqueue_stack.is_empty():
            self.dequeue_stack.push(self.enqueue_stack.pop())

        # Pop the item from dequeue_stack
        return self.dequeue_stack.pop()
