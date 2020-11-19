"""
Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle. As if waiting in a queue for the movie
tickets, the first one to stand in line is the first one to buy a ticket and enjoy the movie.


https://www.geeksforgeeks.org/queue-in-python/
https://docs.python.org/3/library/asyncio-queue.html
"""

##########
# Python program to demonstrate queue implementation using list

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

# dequeue
queue.pop(0)
queue.pop(0)
print(queue)

# front
print(queue[0])

# rear
print(queue[-1])

##########
# Python program to demonstrate queue implementation using collections.deque

from collections import deque

queue_deque = deque()

# enqueue
queue_deque.append(1)
queue_deque.append(2)
queue_deque.append(3)
queue_deque.append(4)
queue_deque.append(5)
print(queue_deque)

# dequeue
queue_deque.popleft()
queue_deque.popleft()

##########
# Python program to demonstrate queue implementation using queue.Queue


from queue import Queue

queue_q = Queue()

# enqueue
queue_q.put(1)
queue_q.put(2)
queue_q.put(3)
queue_q.put(4)
queue_q.put(5)
print(queue_q)

# dequeue
queue_q.get()
queue_q.get()
print(queue_q)
