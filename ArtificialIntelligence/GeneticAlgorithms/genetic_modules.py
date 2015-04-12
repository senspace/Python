#   coding = utf-8
#   Application Modules

import random

def randk(i,j):
    t = random.randint(i,j)
    return t

def bin2dec(string_num):
	return int(string_num, 2)

def dec2bin(num):
	k = '000'
	i = bin(num)
	if num <= 1:
		k = '00' + i[2]
	elif num <= 3:
		k = '0' + i[2:4]
	elif num <= 7:
		k = i[2:]
	else:
		k = i
	return k

def add_bin(x1, x2):
	x = x1 + x2
	return x

#init colony for four idiotypes
def init_gene():
	a = 0
	node = []
	node_temp = []
	while (a < 4):
		i = randk(0, 7)
		j = randk(0, 7)
		result = i*i + j*j
		m = dec2bin(i)
		n = dec2bin(j)
		data = add_bin(m, n)
		node.append(Node(data, result))
		node_temp.append(Node(data, result))
		a = a + 1
	return node

def fitness(node):
	a = 0
	fit = [0, 0, 0, 0]
	total = node[0].result + node[1].result + node[2].result + node[3].result
	while(a < 4):
		fit[a] = int(round(node[a].result * 100.0 / total))
		a = a + 1
	return fit

def select(fit):
	a = 0
	total = 0
	element = [0, 0, 0, 0]
#	 print("total:")
	while (a < 4):
		total += fit[a]
		a += 1
#	 print(total)
#	 print(0, fit[0], fit[0]+fit[1], fit[0]+fit[1]+fit[2], fit[0]+fit[1]+fit[2]+fir[3])
	a = 0
	while(a < 4):
		p = randk(1, total)
#		 print(p)
		if p > 0 and p <= fit[0]:
			element[a] = 0  
		elif p > fit[0] and p <= (fit[0]+fit[1]):
			element[a] = 1 
		elif p > (fit[0]+fit[1]) and p <= (fit[0]+fit[1]+fit[2]):
			element[a] = 2
		elif p > (fit[0]+fit[1]+fit[2]) and p <= total:
			element[a] = 3
		else:
			print("random error!")
#		 print(element[a])
		a += 1
	return element

#	mate randomly
#	p = 1 : node[0] --- node[1]
#	p = 2 : node[0] --- node[2]
#	p = 3 : node[0] --- node[3]
#	point of connection: k - [1:5]
def mate(node, node_temp):
	p = randk(1, 3)
	match = [0, 1, 2, 3]
	if p == 1:
		match = [0, 1, 2, 3]
	elif p == 2:
		match = [0, 2, 1, 3]
	elif p == 3:
		match = [0, 3, 1, 2]

	k1 = randk(1, 5)
	k2 = randk(1, 5)

	print("mate:")
	print(match[0], match[1], match[2], match[3], k1, k2)

	node_temp[0].data = node[match[0]].data[:k1] + node[match[1]].data[k1:]
	node_temp[1].data = node[match[1]].data[:k1] + node[match[0]].data[k1:]
	node_temp[2].data = node[match[2]].data[:k2] + node[match[3]].data[k2:]
	node_temp[3].data = node[match[3]].data[:k2] + node[match[2]].data[k2:]
	a = 0
	while(a < 4):
		m = bin2dec(node_temp[a].data[:3])
		n = bin2dec(node_temp[a].data[3:])
		node_temp[a].result = m*m + n*n
		a += 1

	print(node_temp[0].data)
	print(node_temp[1].data)
	print(node_temp[2].data)
	print(node_temp[3].data)

	return node_temp

def variation(node, node_temp):
	a = 0
	print("variation")
	while(a < 4):
		p = randk(0, 5)
#		 print(p)
		
		if node_temp[a].data[p] == '0':
			node_temp[a].data = node_temp[a].data[0:p] + '1' + node_temp[a].data[p+1:]
		a += 1

	print(node_temp[0].data)
	print(node_temp[1].data)
	print(node_temp[2].data)
	print(node_temp[3].data)

	return node_temp 















































