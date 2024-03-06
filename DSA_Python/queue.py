# implemeneting Queue class using collecions.deque

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        return self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.queue)
q.dequeue()
print(q.queue)
print(q.size())
print(q.is_empty())


#using list as queue

stock_prices = []

stock_prices.insert(0, 101)
stock_prices.insert(0, 102)
stock_prices.insert(0, 103)
stock_prices.insert(0, 104)

print(stock_prices)

stock_prices.pop()
print(stock_prices)
stock_prices.pop()
print(stock_prices)
stock_prices.pop()
print(stock_prices)
