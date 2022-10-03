class EmptyError(Exception):
    pass

class DList:
    class Node:
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_before(self, item, target):
        n = self.Node(item, target.prev, target)
        target.prev.next = n
        target.prev = n
        self.size += 1

    def insert_after(self, item, target):
        n = self.Node(item, target, target.next)
        target.next.prev = n
        target.next = n
        self.size += 1

    def delete(self, item):
        item.prev.next = item.next
        item.next.prev = item.prev
        self.size -= 1

    def print_list(self):
        d = self.head.next
        while d != self.tail:
            if self.is_empty(): print("List is Empty!")
            else:
                if(d.next != self.tail):
                    print(d.item, " <=> ", end='')
                else:
                    print(d.item)
                d = d.next
