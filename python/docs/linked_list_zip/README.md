# Linked_list_zip
This program defines a Node class and a LinkedList class to create and manipulate linked lists. Additionally, it includes a function zip_lists that merges two linked lists (referred to as list_a and list_b) into a single linked list by alternating their elements. If one list is shorter, the function continues with the elements of the longer list after the end of the shorter one. 

## Whiteboard Process
To be added

## Approach & Efficiency
* __Time Complexity:__ The time complexity of zip_lists is determined by how long it takes to merge the two lists. The function iterates through both lists simultaneously, stopping when it reaches the end of one (or both) of the lists. In the worst-case scenario, this means iterating through all elements of the longer list. If n and m are the lengths of the two lists, the time complexity is O(max(n, m)), since the function iterates through the nodes of both lists at most once.
* __Space Complexity:__ The space complexity of the algorithm is O(1), which means it's constant. This is because the function only creates a few pointers (like current_a, current_b, next_a, and next_b) and does not allocate any additional data structures that grow with the size of the input. The merging is done in place by rearranging the pointers of the existing nodes in the input lists.

## Solution
See __linked_list_zip.py__
