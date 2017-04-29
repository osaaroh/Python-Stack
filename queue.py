#queue implementation first in first out. enqueue and dequeue
class MyQueue(object):
    def __init__(self):
        self.items = []
        self.max = 10

    def displayItems (self):
        print self.items

    def enqueue(self, item):
        if len(self.items) != self.max:
            self.items.append(item)
        else:
            print 'Queue overload'

    def dequeue(self):
        if self.items == []:
            print 'Underflow Error'
        else:
            del self.items[0]

do = MyQueue()
do.enqueue(1)
do.enqueue(2)
do.enqueue(3)
do.enqueue(4)
do.enqueue(5)
do.enqueue(6)
do.enqueue(7)
do.enqueue(8)
do.enqueue(9)
do.enqueue(10)
do.enqueue(11)
do.displayItems()
do.dequeue()
do.dequeue()
do.dequeue()
do.displayItems()