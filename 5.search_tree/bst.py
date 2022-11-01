class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:

    # 트리 생성자
    def __init__(self):
        self.root = None

    # 탐색 연산
    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, key):
        if n.key == key:
            return n.value
        elif n.key > key:
            self.get_item(n.left, key)
        else:
            self.get_item(n.right, key)

    # 삽입 연산
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self): # 최솟값 가진 노드 찾기
        return self.min_item(self.root)

    def min_item(self, n):
        if n.left is None:
            return n
        return n.left

    def delete_min(self):   # 최솟값 삭제
        if self.root == None:
            print("Tree is empty")
        self.root = self.delete_min_item()

    def delete_min_item(self, n):
        if n.left is None:
            return n.right
        n.left = self.delete_min_item(n.left)
        return n

    def delete(self, key):  # 삭제 연산
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
        return n

    # 전위순회 : n, 왼쪽, 오른쪽
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
            print(str(n.value), '', end='')

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

    #트리 높이 계산
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1


if __name__ == '__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n레벨순회:\t', end='')
    t.levelorder(t.root)
    print('\n200 삭제 후:')
    t.delete(200)
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n레벨순회:\t', end='')
    t.levelorder(t.root)



