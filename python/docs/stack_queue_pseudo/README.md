# PseudoQueue Implementation

Description of the challenge:

The challenge is to implement a queue using two stacks. This involves creating a PseudoQueue class that mimics the behavior of a standard queue (FIFO - First In, First Out) using only stack operations (LIFO - Last In, First Out). The PseudoQueue class should have two primary methods: enqueue for adding elements to the queue and dequeue for removing elements from the queue.


## Approach & Efficiency

The approach taken was to use two stacks, __enqueue_stack__ and __dequeue_stack__.

* For __enqueue__, the algorithm transfers all elements from __dequeue_stack__ to __enqueue_stack__ and then adds the new element.
* For __dequeue__, it reverses the process by transferring elements back to __dequeue_stack__ before popping the top element.
This approach ensures that the oldest element (first in) is always at the top of __dequeue_stack__, allowing FIFO behavior.

### Efficiency:

* __Time Complexity:__
    - For enqueue, the worst-case time complexity is O(n) due to the transfer of elements between stacks.
    - For dequeue, it's also O(n) for the same reason.
* Space Complexity: O(n), where n is the number of elements in the queue. This is due to the additional stack used for transferring elements.
Solution

To run the code, ensure you have a Python environment set up. Then, use the PseudoQueue class as __follows:__
```
pq = PseudoQueue()
pq.enqueue(1)
pq.enqueue(2)
print(pq.dequeue()) # Outputs: 1
pq.enqueue(3)
print(pq.dequeue()) # Outputs: 2
```
### Examples
Enqueueing and Dequeueing Single Item:
```
pq = PseudoQueue()
pq.enqueue("apple")
print(pq.dequeue())  # Output: "apple"
```
Enqueueing Multiple Items and Dequeueing Them:
```
pq = PseudoQueue()
pq.enqueue("apple")
pq.enqueue("banana")
pq.enqueue("cherry")
print(pq.dequeue())  # Output: "apple"
print(pq.dequeue())  # Output: "banana"
print(pq.dequeue())  # Output: "cherry"
```


