from bstree import *
    
"""
	Let us create following BST
		50
	   /  \
	 30	   70
	 / \   / \
	20 40 60 80

"""

tree = BSTree()

tree.insert(16)
tree.insert(7)
tree.insert(3)
tree.insert(1)
tree.insert(12)
tree.insert(20)
tree.insert(17)

print()
print('Pre-Order Traverse: ', end="")
tree.preVisit()
print('In-Order Traverse: ', end="")
tree.inVisit()
print('Post-Order Traverse: ', end="")
tree.postVisit()
print('Breadth-First Traverse: ', end="")
tree.breadth_first(); print()
print()

do = input('   - Delete: ').split() 
tree.delete(int(do[0]))

print()
print('Pre-Order Traverse: ', end="")
tree.preVisit()
print('In-Order Traverse: ', end="")
tree.inVisit()
print('Post-Order Traverse: ', end="")
tree.postVisit()
print('Breadth-First Traverse: ', end="")
tree.breadth_first()
print()