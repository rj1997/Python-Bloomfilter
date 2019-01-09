from bitarray import bitarray
import mmh3

import sys
import string
import random
import queue

class BloomFilter(object):

	def __init__(self, size, hashcount):
		self.size = size
		self.hashcount = hashcount
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
		print("BloomFilter initialized with size : ",self.size," & hashcount : ",self.hashcount)

	def add(self,string):
		for seed in range(self.hashcount):
			result = mmh3.hash(string,seed)%self.size
			self.bit_array[result] = 1

	def index(self,string):
		returnval = []
		for seed in range(self.hashcount):
			result = mmh3.hash(string,seed)%self.size
			returnval.append(result)
		return returnval

	def isPresent(self,string):
		for seed in range(self.hashcount):
			result = mmh3.hash(string,seed)%self.size
			if self.bit_array[result] == 0:
				return False
		return True

def generateRandomString(maxstringlength):
	chars = string.ascii_letters + string.digits
	size = random.randint(1,maxstringlength)
	return ''.join(random.choice(chars) for _ in range(size))


if sys.argv[1] == "basic":

	setOfStrings = set()

	size = int(input("Enter size of bloomfilter : "))
	hashnum = int(input("Enter no. of hashes of bloomfilter : "))
	queries = int(input("Enter no. of queries : "))
	bf = BloomFilter(size,hashnum)

	totaltries = 0
	total_false_positive = 0
	total_false_negative = 0

	for i in range(queries):

		totaltries = totaltries + 1

		inputstring = input("Input a string to check : ")
		print("BF says isPresent? : ",bf.isPresent(inputstring))

		sethas = False
		if inputstring in setOfStrings:
			sethas = True
		print("Real analysis is Present? : ", sethas)

		if bf.isPresent(inputstring) and not sethas:
			print('False positive encountered')
			total_false_positive = total_false_positive + 1

		if  sethas and not bf.isPresent(inputstring):
			print('False negative encountered')
			total_false_negative = total_false_negative + 1

		print('Hit ratio : ',1-(total_false_negative+total_false_positive)/totaltries)
		print("Total false positive : ",total_false_positive)
		print("Total false negative : ",total_false_negative)

		if not bf.isPresent(inputstring):
			setOfStrings.add(inputstring)
			bf.add(inputstring)


if sys.argv[1] == "simulation":

	setOfStrings = set()

	size = int(input("Enter size of bloomfilter : "))
	hashnum = int(input("Enter no. of hashes of bloomfilter : "))
	queries = int(input("Enter no. of queries : "))
	maxstringlength = int(input("Enter max string length : "))
	bf = BloomFilter(size,hashnum)

	totaltries = 0
	total_false_positive = 0
	total_false_negative = 0

	for i in range(queries):

		totaltries = totaltries + 1

		inputstring = generateRandomString(maxstringlength)
		print('Generated string is : ',inputstring)

		print("BF says isPresent? : ",bf.isPresent(inputstring))

		sethas = False
		if inputstring in setOfStrings:
			sethas = True
		print("Real analysis is Present? : ", sethas)

		if bf.isPresent(inputstring) and not sethas:
			print('False positive encountered')
			total_false_positive = total_false_positive + 1

		if  sethas and not bf.isPresent(inputstring):
			print('False negative encountered')
			total_false_negative = total_false_negative + 1

		print('Hit ratio : ',1-(total_false_negative+total_false_positive)/totaltries)
		print('Calculated prob : ',pow((1-pow((1-1/size),hashnum*queries)),hashnum))
		print("Total false positive : ",total_false_positive)
		print("Total false negative : ",total_false_negative)


		if not bf.isPresent(inputstring):
			setOfStrings.add(inputstring)
			bf.add(inputstring)

if sys.argv[1]=="remote-cache-simulation":

	setOfStrings = set()

	size = int(input("Enter size of bloomfilter : "))
	hashnum = int(input("Enter no. of hashes of bloomfilter : "))
	queries = int(input("Enter no. of queries : "))
	cache_size = int(input("Enter cache_size : "))
	maxstringlength = int(input("Enter max string length : "))
	bf = BloomFilter(size,hashnum)

	q = queue.Queue(maxsize=cache_size)
	count_array = [0]*size

	totaltries = 0
	total_false_positive = 0
	total_false_negative = 0
	total_hit_count = 0

	for i in range(queries):

		totaltries = totaltries + 1

		inputstring = generateRandomString(maxstringlength)
		print('Generated string is : ',inputstring)

		print("BF says isPresent? : ",bf.isPresent(inputstring))

		if totaltries<=cache_size:
			if not bf.isPresent(inputstring):
				q.put(inputstring)
				if not bf.isPresent(inputstring):
					bf.add(inputstring)
			else:
				total_hit_count = total_hit_count + 1
		else:
			if not bf.isPresent(inputstring):
				item = q.get()
				for ind in bf.index(inputstring):
					count_array[ind] = count_array[ind] - 1
					if count_array[ind]==0:
						zeroize(ind)
				q.put(inputstring)
				bf.add(inputstring)
			else:
				total_hit_count = total_hit_count + 1

		print("Hit ratio : ",total_hit_count/totaltries)


		