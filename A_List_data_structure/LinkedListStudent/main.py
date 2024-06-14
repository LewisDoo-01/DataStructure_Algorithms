from node import Node
from student import Student
from linked_list import LinkedList
 
a_llist = LinkedList()
 
print()
print('             Menu')
print('--------------------------------')
print('   - insert at beg')
print('   - insert at end')
print('   - insert before <index>')
print('   - insert after <index>')
print('   - remove <index>') 
print('   - quit')    

while True:
    print('The list: ')
    a_llist.display()
    print()
    
    do = input('What would you like to do? ').split() 
    operation = do[0].strip().lower() 
    
    if operation == 'insert':  
        suboperation = do[1].strip().lower()
        position = do[2].strip().lower()         
        if suboperation == 'at':
            if position == 'beg':
                id = input('   - Enter id: ')
                name = input('   - Enter name: ')
                mark = float(input('   - Enter mark: '))
                a_llist.insert_at_beg(Node(Student(id, name, mark)))
            elif position == 'end':
                id = input('   - Enter id: ')
                name = input('   - Enter name: ')
                mark = float(input('   - Enter mark: '))
                a_llist.insert_at_end(Node(Student(id, name, mark)))
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                id = input('   - Enter id: ')
                name = input('   - Enter name: ') 
                mark = float(input('   - Enter mark: '))
                a_llist.insert_after(ref_node, Node(Student(id, name, mark)))
            elif suboperation == 'before':
                id = input('   - Enter id: ')
                name = input('   - Enter name: ')
                mark = float(input('   - Enter mark: '))
                a_llist.insert_before(ref_node, Node(Student(id, name, mark)))
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.remove(node)
 
    elif operation == 'quit':
        break