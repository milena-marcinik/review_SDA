"""
A stack is a last-in-first-out (LIFO) data structure.

https://www.educative.io/edpresso/how-to-implement-stack-in-python
https://www.geeksforgeeks.org/stack-in-python/
"""


"""
# Stack implementation using list
"""

stack = []

# push:
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

# peek:
print(stack[-1])

# pop:
stack.pop()
stack.pop()
print(stack)


"""
Stack implementation using collections.deque.

Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of the 
container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides 
O(n) time complexity. 
"""


from collections import deque


stack_deque = deque()

stack_deque.appendleft(3)
stack_deque.appendleft(4)
stack_deque.appendleft(5)

print(stack_deque.popleft())


"""
Stack implementation using queue module.
"""

from queue import LifoQueue


