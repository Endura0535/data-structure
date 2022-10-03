from slist import SList
from dlist import DList

'''
if __name__ == '__main__':
    s = SList()
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_front('pear')
    s.insert_after('cherry', s.head)
    s.print_list()
    #print('cherry는 %d번째' % s.search('cherry'))
'''

if __name__ == '__main__':
    d = DList()
    d.insert_after('apple', d.head)
    d.insert_before('orange', d.tail)
    d.insert_before('cherry', d.tail)
    d.insert_after('pear', d.head.next)
    d.delete(d.head.next.next)
    d.print_list()

