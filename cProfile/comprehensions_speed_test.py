INPUT_LIST = range(10000)

def lists_with_for_loop():
	'''
	'''
	evens = []
	for item in INPUT_LIST:
		if item % 2 == 0:
			evens.append(item)


def lists_with_comprehensions():
	'''
	'''
	evens = [x for x in INPUT_LIST if x % 2 == 0]

if __name__ == '__main__':
	lists_with_for_loop()
	lists_with_comprehensions()
