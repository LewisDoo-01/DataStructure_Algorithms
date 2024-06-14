class Hash(object):
	def __init__(self, bucket):
		# Number of buckets
		self.__bucket = bucket
		# Hash table of size bucket
		self.__table = [[] for _ in range(bucket)]

	# hash function to map values to key
	def hashFunction(self, key):
		ascii = ord(key[0])
		if ascii >= 65 and ascii <= 90: # kí tự in hoa
			return ord(key[0]) - 65
		elif ascii >= 97 and ascii <= 122: # kí tự thường
			return ord(key[0]) - 97
		else:
			return -1

	def insertItem(self, key):
		# get the hash index of key
		index = self.hashFunction(key.Name)
		self.__table[index].append(key)
	
	# function to display hash table
	def displayHash(self):
		for i in range(self.__bucket):
			print("[%d]" % i, end='')
			for x in self.__table[i]:
				print(' --> ', x, end=' ')
			print()