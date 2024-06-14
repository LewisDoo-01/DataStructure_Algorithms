from node import Node
from linked_list import LinkedList


a_llist = LinkedList()

print('Menu')
print('add <data> after <index>')
print('add <data> before <index>')
print('add <data> at begin')
print('add <data> at end')
print('remove <index>')
print('find the largest')
print('find the smallest')
print('quit')
print('sort')

while True:
    print('The list: ', end = '')
    a_llist.display()
    print()

    do = input('What would you like to do?').split()
    operation = do[0].strip().lower()

    if operation == 'add':
        data = int(do[1]) #<data> value
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'begin':
                a_llist.addToHead(new_node)
            elif position == 'end':
                a_llist.addToTail(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.addAfter(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.addBefore(ref_node, new_node)

    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.delete(node)

    elif operation == 'find':
        value = do[2].strip().lower()
        if value == 'smallest':
            print(a_llist.min())
        elif value == 'largest':
            print(a_llist.max())
            print("Minimum element in linked list: ", end="")
    elif operation == 'sort':
        a_llist.bubbleSort()







    elif operation == 'quit':
        break

                    

