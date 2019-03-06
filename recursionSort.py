from itertools import permutations
import random

def isSorted(list):
	for i in range (len(list)-1):
		if list[i]>list[i+1]:
			return False
	return True

def fastSort(list):
	perms = iter(permutations(list,len(list)))
	i = 0
	while isSorted(list) == False:
		list = next(perms)
		i = i+1
	print(i*(len(list)-1))
	temp = []
	for j in range (len(list)):
		temp.append(list[j])
	list = temp
	return list

def recursiveSort(list):
	if len(list)==1:
		return list
	else:
		a = recursiveSort(list[0:len(list)-1])
		a.append(list[len(list)-1])
		random.shuffle(a)
		return fastSort(a)
