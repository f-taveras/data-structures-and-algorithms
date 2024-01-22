class Node:
    """Node class for LinkedList."""

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return str(self.value)


class LinkedList:
    """LinkedList class."""

    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert a new node with the given value to the start of the list."""
        self.head = Node(value, self.head)

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        current = self.head
        while current:
            values.append(str(current))
            current = current.next
        return " -> ".join(values)


def zip_lists(list_a, list_b):
    """Zip two linked lists."""
    if not list_a.head:
        return list_b
    if not list_b.head:
        return list_a

    current_a = list_a.head
    current_b = list_b.head
    while current_a and current_b:
        # Save the next pointers
        next_a = current_a.next
        next_b = current_b.next

        # Link the nodes
        current_a.next = current_b
        if next_a:
            current_b.next = next_a

        # Move to the next pair of nodes
        current_a = next_a
        current_b = next_b

    # If one list is longer, append the rest of it
    if current_b:
        current_a.next = current_b

    return list_a

# Example usage
test_list1 = LinkedList()
test_list2 = LinkedList()

for value in [1, 2, 3]:
    test_list1.insert(value)

for value in ["a", "b", "c"]:
    test_list2.insert(value)

zipped_list = zip_lists(test_list1, test_list2)
print(str(zipped_list))  # Output: 3 -> c -> 2 -> b -> 1 -> a
