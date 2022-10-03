queue = []

def add(item):
    queue.append(item)

def remove():
    return queue.pop(0)

def print_q():
    print(queue)

add('apple')
add('orange')
add('cherry')
print_q()
remove()
print_q()
remove()
print_q