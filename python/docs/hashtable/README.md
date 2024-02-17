# Hash Table

This challenge involves implementing and testing a __Hashtable__ class in Python, ensuring it supports key functionalities such as adding and retrieving key-value pairs, handling collisions, and maintaining a list of all unique keys. The challenge is designed to assess understanding of hash tables, their internal mechanisms like hashing and collision resolution, and the ability to write comprehensive tests using pytest to verify the implementation's correctness and robustness.

## Whiteboard Process
To be added

## Approach & Efficiency
The approach to implementing the Hashtable class involves using an array of __linked lists (separate chaining)__ for collision resolution, ensuring efficient distribution of key-value pairs across the structure. This method allows for __O(1)__ average time complexity for insertion, deletion, and retrieval operations under the assumption of a good hash function and load factor. Efficiency is further optimized by choosing an appropriate initial size and hash function that minimizes collisions, thereby maintaining the performance close to constant time despite varying input sizes and patterns.

## Solution
[Code](../../data_structures/hashtable.py)