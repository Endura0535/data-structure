class binary_heap:

    # 이진힙 생성자 a : 리스트, N : 항목 수
    def __init__(self, a):
        self.a = a
        self.N = len(a) - 1

    # 초기 힙 만들기
    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    # 삽입 연산
    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    # 최솟값 삭제
    def delete_min(self):
        if self.N == 0:
            print("heap 이 비어있음")
            return None
        self.a[1] = self.a[self.N]
        self.a.pop(-1)
        self.N -= 1
        self.downheap(1)

    # 힙 내려가며 힙속성 회복
    def downheap(self, i):
        while self.N > i*2:
            if min(self.a[i], self.a[2*i], self.a[2*i+1]) == self.a[2*i]:
                self.a[i], self.a[2*i] = self.a[2*i], self.a[i]
                i = i*2
            elif min(self.a[i], self.a[2*i], self.a[2*i+1]) == self.a[2*i+1]:
                self.a[i], self.a[2*i+1] = self.a[2*i+1], self.a[i]
                i = i*2+1
        if self.N == i*2 and self.a[i] > self.a[self.N]:
            self.a[i], self.a[self.N] = self.a[self.N], self.a[i]


    # 힙 올라가며 힙속성 회복
    def upheap(self, j):
        while j > 1:
            if self.a[j//2] > self.a[j]:
                self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2

    # 힙 출력
    def print_heap(self):
        for i in range(1, self.N+1):
            print('[', self.a[i], ']')
        print("항목수 = ", self.N)

a = [None,90,80,70,50,60,20,30,35,10,15,45,40]
b = binary_heap(a)
print("힙 만들기 전: ")
b.print_heap()
b.create_heap()
print("최소힙:")
b.print_heap()
print("최솟값 삭제 후")
b.delete_min()
b.print_heap()
b.insert(5)
print("5 삽입 후")
b.print_heap()
