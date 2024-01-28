# Binary Tree
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency

* Time Complexity: __O(n)__, where n is the number of nodes in the tree. This is because each node is visited exactly once during the traversal.
* Space Complexity: __O(h)__, where h is the height of the tree. This space complexity accounts for the call stack during the recursive traversal. In the worst case (a completely unbalanced tree), this could be O(n).

# BinarySearchTree:

Time Complexity:
Average Case: O(log n), for a balanced tree, because you eliminate half of the tree to search in each step.
Worst Case: O(n), for a completely unbalanced tree (e.g., when every node only has a left or right child), the algorithm degrades to a linear search.
Space Complexity: O(h) due to the recursion stack, which in the worst case can become O(n) for an unbalanced tree.
contains Method:

Time Complexity:
Average Case: O(log n), as each comparison allows the algorithm to skip about half of the tree.
Worst Case: O(n), in the case of an unbalanced tree, it can degrade to searching through each node linearly.
Space Complexity: O(h), which in the worst case can be O(n) due to the recursion stack in an unbalanced tree.

## Solution
[See the Code](../../data_structures/binary_tree.py)
