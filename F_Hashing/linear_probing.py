# Python3 implementation of the Linear Probing

# Function to print an array
def printArray(arr, n):
	# Iterating and printing the array
	for i in range(n):
		print(arr[i], end=" ")

# Function to implement the linear probing
def hashing(table, tsize, arr, N):
	# Iterating through the array
	for i in range(N):
		# Computing the hash value
		hv = arr[i] % tsize
		# Insert in the table if there is no collision
		if (table[hv] == -1):
			table[hv] = arr[i]
		else:
			# If there is a collision
			# iterating through all possible linear values
			for j in range(tsize):
				# Computing the new hash value
				t = (hv + j) % tsize
				if (table[t] == -1):
					# Break the loop after inserting the value
					# in the table
					table[t] = arr[i]
					break
	printArray(table, N)

# Driver code
if __name__ == "__main__":
	arr1 = [50, 700, 76, 85, 92, 73, 101]
	arr2 = [4, 0, 18, 24, 16, 20, 4, 18, 19, 8, 14, 13]
	N = 12
	# Size of the hash table
	L = 16
	hash_table = [0] * 16
	# Initializing the hash table
	for i in range(L):
		hash_table[i] = -1
	# Function call
	hashing(hash_table, L, arr2, N)
# This code is contributed by code_hunt