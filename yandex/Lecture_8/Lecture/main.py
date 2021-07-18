def find(memstruct, root, x):
	key = memstruct[0][root][0]
	if k == key:
		return root
	elif x < key:
		left = memstruct[0][root][1]
		if left == -1:
			return -1
		else:
			return find(memstruct, left, x)
	elif x > key:
		right = memstruct[0][root][2]
		if right == -1:
			return -1
		else:
			return find(memstruct, right, x)
