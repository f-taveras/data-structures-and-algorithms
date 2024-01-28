class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        return self._traverse_pre_order(self.root, [])

    def _traverse_pre_order(self, node, elements):
        if node:
            elements.append(node.value)
            self._traverse_pre_order(node.left, elements)
            self._traverse_pre_order(node.right, elements)
        return elements

    def in_order(self):
        return self._traverse_in_order(self.root, [])

    def _traverse_in_order(self, node, elements):
        if node:
            self._traverse_in_order(node.left, elements)
            elements.append(node.value)
            self._traverse_in_order(node.right, elements)
        return elements

    def post_order(self):
        return self._traverse_post_order(self.root, [])

    def _traverse_post_order(self, node, elements):
        if node:
            self._traverse_post_order(node.left, elements)
            self._traverse_post_order(node.right, elements)
            elements.append(node.value)
        return elements

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

