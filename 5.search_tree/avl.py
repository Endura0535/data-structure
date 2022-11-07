'''
AVL tree
'''

class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height

    # 삽입 연산
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    # 불균형 처리 : (노드 n의 왼쪽 서브트리 높이) - (오른쪽 서브트리 높이) 
    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    # 최솟값 가진 노드 찾기
    def min(self):
        return self.min_item(self.root)

    def min_item(self, n):
        if n.left is None:
            return n
        return n.left

    # 최솟값 삭제
    def delete_min(self):
        if self.root == None:
            print("Tree is empty")
        self.root = self.delete_min_item()

    def delete_min_item(self, n):
        if n.left is None:
            return n.right
        n.left = self.delete_min_item(n.left)
        return n

    # 삭제 연산
    def delete(self, key):
        self.root = self.delete_item(self.root, key)

    def delete_item(self, n, key):
        if n is None:
            return None
        elif n.key > key:
            n.left = self.delete_item(n.left, key)
        elif n.key < key:
            n.right = self.delete_item(n.right, key)
        else:
            if n.left is None:
                return n.right
            if n.right is None:
                return n.left
            target = n
            n = self.min_item(target.right)
            n.right = self.delete_min_item(target.right)
            n.left = target.left
        return self.balance(n)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def preorder(self, n):
        if n != None:
            print(str(n.key), '', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위순회 : 왼쪽, n, 오른쪽
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), '', end='')
            if n.right:
                self.inorder(n.right)

    # 후위순회 : 왼쪽, 오른쪽, n
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key), '', end='')

    # 레벨순회 : 최상위 노드부터 각 레벨별로 왼쪽 오른쪽
    def levelorder(self, root):
        q = []
        q.append(root)
        while q:
            t = q.pop(0)
            print(str(t.key),'',end='')
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

if __name__ == '__main__':
    t = AVL()
    t.put(75, 'apple')
    t.put(80, 'banana')
    t.put(85, 'melon')
    t.put(20, 'orange')
    t.put(10, 'lime')
    t.put(50, 'kiwi')
    t.put(30, 'grape')
    t.put(40, 'peach')
    t.put(70, 'cherry')
    t.put(90, 'pear')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n75와 85 삭제 후:')
    t.delete(75)
    t.delete(85)
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)