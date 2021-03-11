'''
Queues are like lists and sequences but thr difference is that they have a specific order of how elements get into this lists and how
to access them to get them out of this lists.
'''

import queue
#First in First out Queue
q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number)

print(q.get())
print(q.get()) #prints the next number in the queue

#Last in First out queue
q = queue.LifoQueue()

numbers = [1, 2, 3, 4, 5, 6, 7]
for x in numbers:
    q.put(x)

print(q.get())

#Priority Queue - The least gets the highest priority and vice versa
q = queue.PriorityQueue()

q.put((2, 'Hello world!'))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())