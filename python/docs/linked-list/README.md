# Linked List
This programming challenge involves the creation and enhancement of a custom __LinkedList__ class in Python. The __LinkedList__ class is designed to represent a basic linked list data structure, featuring various methods for typical linked list operations. These operations include inserting new elements at the beginning of the list, checking if the list is empty, determining if a particular value exists within the list, and generating a string representation of the list's contents.

## Whiteboard Process
[White Board](./whiteboard.png)

## Approach & Efficiency
* __Space Complexity:__ O(n)
* __Time Complexity:__
    - Initialization, Check if Empty, Insert: __O(1)__
    - String Representation, Includes: __O(n)__

## Solution
* __Usage code:__

```
my_list = LinkedList()

# Checking if the list is empty
print("Is the list empty?", my_list.is_empty())  # Expected output: True

# Inserting elements
my_list.insert("apple")
my_list.insert("banana")

# Checking if the list is still empty
print("Is the list empty after insertions?", my_list.is_empty())  # Expected output: False

# Printing the list
print("Current list:", my_list)  # Expected output: { banana } -> { apple } -> NULL

# Checking if an element is in the list
print("Does the list include 'apple'?", my_list.includes("apple"))  # Expected output: True
print("Does the list include 'orange'?", my_list.includes("orange"))  # Expected output: False
```