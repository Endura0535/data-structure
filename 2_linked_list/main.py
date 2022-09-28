from slist import SList
if __name__ == '__main__':
    s = SList()
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_front('pear')
    s.insert_after('cherry', s.head)
    s.print_list()
    #print('cherry는 %d번째' % s.search('cherry'))