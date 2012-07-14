import numpy as N

SPARSE_INPUT_LIST = N.random.random_integers(0,1000,10000)
DENSE_INPUT_LIST = N.random.random_integers(0,10,10000)

# ---------------------------------------------------------------------------- 
# Functions
# ---------------------------------------------------------------------------- 

def unique_with_for_loop_dense():
	output = []
	for item in DENSE_INPUT_LIST:
		if item not in output:
			output.append(item)

# ---------------------------------------------------------------------------- 

def unique_with_for_loop_sparse():
	output = []
	for item in SPARSE_INPUT_LIST:
		if item not in output:
			output.append(item)

# ---------------------------------------------------------------------------- 

def unique_with_set_dense():
	output = set(DENSE_INPUT_LIST)

# ---------------------------------------------------------------------------- 

def unique_with_set_sparse():
	output = set(SPARSE_INPUT_LIST)

# ---------------------------------------------------------------------------- 
# For command line execution.
# ----------------------------------------------------------------------------

if __name__ == '__main__':
	unique_with_for_loop_dense()
	unique_with_for_loop_sparse()
	unique_with_set_dense()
	unique_with_set_sparse()
