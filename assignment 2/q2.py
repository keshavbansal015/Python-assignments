""" my_filter function similar to python's filter function """

def my_filter(func,itr):
	itr = [x for x in itr if func(x) == True]
	return itr

def func(x):
	return x<10

lis = [1,3,1,2,42,21,24,1,212,3,213,124,1]
print(my_filter(func,lis))
