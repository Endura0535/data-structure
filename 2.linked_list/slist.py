class EmptyError(Exception):
    pass

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self): return self.size    # 리스트 사이즈 리턴
    def is_empty(self): return self.size == 0   # 리스트가 비었는지 확인

    def insert_front(self, item):   # 리스트 맨 앞에 item 삽입
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item,self.head)
        self.size += 1

    def insert_after(self, item, p):    # item을 p 뒤에 삽입
        p.next = self.Node(item, p.next)
        self.size += 1

    def delete_front(self): # 맨 앞의 item 삭제
        if self.is_empty():
            raise EmptyError
        else:
           self.head = self.head.next
           self.size -= 1

    def delete_after(self, item): # item 뒤의 원소를 삭제
        if self.is_empty():
            raise EmptyError
        item.next = item.next.next
        self.size -= 1

    def search(self,item): # item의 index를 찾아 반환
        t = self.head
        for k in range(self.size):
            if item == t.item:
                return k
            t = t.next
        return None

    def print_list(self): # 리스트 출력
       p = self.head
       for k in range(self.size):
           if p.next != None:
               print(p.item, ' -> ', end='')
           else:
               print(p.item)
           p = p.next