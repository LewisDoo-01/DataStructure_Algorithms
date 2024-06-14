from node import Node
from linked_list import DoublyLinkedList
 
a_dllist = DoublyLinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_dllist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_dllist.insert_at_beg(new_node)
            elif position == 'end':
                a_dllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_dllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_dllist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_dllist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_dllist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_dllist.remove(node)
 
    elif operation == 'quit':
        break