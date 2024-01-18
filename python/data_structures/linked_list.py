class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    """
    LinkedList implements a basic linked list data structure. It supports operations like
    insertion of new data at the beginning, checking if the list is empty, searching for
    a value within the list, and generating a string representation of the list contents.
    """
   

    def __init__(self):
        self.head = None
        

    def is_empty(self):
        return self.head is None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        if self.is_empty():
            return "Literally nothing to see here"
        
        current_node = self.head
        elements = []
        while current_node:
            elements.append(f"{{ {current_node.data} }}")
            current_node = current_node.next
        elements.append("NULL")
        return " -> ".join(elements)
    
    def includes(self,data):
        current_node = self.head 
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k cannot be negative")

        length = self.length()
        if k >= length:
            raise TargetError("k is out of range")

        target_index = length - k - 1
        current = self.head
        for _ in range(target_index):
            current = current.next
        
        return current.data

class TargetError(Exception):
    def __init__ (self, message="Target operation error in LinkedList"):
        self.message = message
        super().__init__(self.message)

