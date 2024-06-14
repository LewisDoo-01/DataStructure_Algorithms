import array as arr

a = arr.array('i', [1, 2, 4, 5])
for i in range(0, 4):
	print(a[i], end=" ")
print()
	
a.insert(2, 3); a.append(6)
sliced_array = a[0:6]
print(sliced_array)

print(a.pop(2))

a.remove(6); a.reverse()
for i in a:
    print(i, end=" ")