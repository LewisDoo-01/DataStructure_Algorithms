# Built-in Data Structures in python

# Lists
my_list = []
print(my_list)
my_list = [1, 2, 3, 'example', 3.132]
print(my_list)
print(my_list[3])
print(my_list[0:2])
my_list.append(['S001', 'Nguyen Van Loc', 7.5])
print(my_list)
del my_list[2]
print(my_list)
my_list.remove('example')
print(my_list)
a = my_list.pop(1)
print('Popped Element: ', a, ' List remaining: ', my_list)
my_list.clear()
print(my_list)

# Dictionary
my_dict = {}
print(my_dict)
my_dict = {1: 'Python', 2: 'Java', 3: 'Ruby'}
print(my_dict)
print(my_dict[2])
print(my_dict.get(3))
my_dict[2] = 'C++'
print(my_dict)
a = my_dict.pop(3)
print('Value:', a)
print('Dictionary:', my_dict)
my_dict.clear()
print(my_dict)

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[:])
my_tuple = my_tuple + (4, 5, 6)
print(my_tuple)

# Sets
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)







