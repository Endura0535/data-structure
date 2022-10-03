stack = []

def push(item):     # append 메소드를 통해 리스트 맨 뒤에 item 추가
    stack.append(item)

def peek():     # 리스트 맨 뒤 항목 반환
    if stack:
        return(stack[-1])

def pop():      # 리스트 맨 뒤 항목 제거 및 반환
    if stack:
        return stack.pop(-1)

push('apple')
push('orange')
push('cherry')
print(stack)
print('top항목: ', peek())
print(pop())
print(pop())
print(pop())
print(stack)