class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class binary_tree:
    def __init__(self):
        self.root = None

    # 전위순회 : n, 왼쪽, 오른쪽
    def preorder(self, n):
        if n != None:
            print(str(n.item), '', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위순회 : 왼쪽, n, 오른쪽
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item), '', end='')
            if n.right:
                self.inorder(n.right)

    # 후위순회 : 왼쪽, 오른쪽, n
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), '', end='')

    # 레벨순회 : 최상위 노드부터 각 레벨별로 왼쪽 오른쪽
    def levelorder(self, root):
        q = []
        q.append(root)
        while q:
            t = q.pop(0)
            print(str(t.item),'',end='')
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

    #트리 높이 계산
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1

t = binary_tree()

n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')
n8 = Node('H')

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n4.right = n7
n5.left = n8

t.root = n1

print('트리 높이 = ', t.height(t.root))
print('전위순회 : ')
t.preorder(t.root)
print('\n중위순회 : ')
t.inorder(t.root)
print('\n후위순회 : ')
t.postorder(t.root)
print('\n레벨순회 : ')
t.levelorder(t.root)
