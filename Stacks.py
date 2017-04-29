#Stack implementation. Last in first out. Push and pop
class MyStack(object):
    def __init__(self):
        self.items = []
        items = self.items

    def displayStack(self):
        print self.items

    def push(self, obj):
        items = self.items
        items.append(obj)

    def pop(self):
        items = self.items
        newItems = items.pop()
        return newItems

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def peek(self):
        X = len(self.items) - 1
        return self.items[X]



ly = MyStack()
ly.push(1)
ly.push(2)
ly.push(3)
print ly.peek()
ly.displayStack()
ly.pop()
ly.pop()
ly.displayStack()
print ly.is_empty()
print ly.peek()
