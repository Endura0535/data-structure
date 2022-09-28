class EmptyError(Exception):
    pass

class CList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next
    def __init__(self):
        self.last = None
        self.size = 0
    def no_items(self): return self.size
    def is_empty(self): return self.size==0

    def insert(self, item): # 첫 노드로 삽입
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):    #첫 노드의 아이템 반환
        if self.is_empty():
            raise EmptyError
        else:
            return self.last.next.item

    def delete(self):   #첫 노드 삭제
        if self.is_empty(): raise EmptyError('Underflow')
        if self.size == 1:
            self.last = None
        else:
            self.last.next = self.last.next.next
        self.size -= 1
        return self.last.next.item

    def print_list(self):
        if self.is_empty():
            print("Empty List")
        else:
            p = self.last.next
            while p.next != self.last.next:
                print(p.item,' -> ', end='')
                p = p.next
            print(p.item)