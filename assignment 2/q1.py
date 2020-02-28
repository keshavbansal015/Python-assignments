""" my_reduce function similar to python's reduce function """

def my_reduce(func,itr):
	l1 = itr.pop(0)
	try:
		l2 = itr.pop(0)
	except:
		return l1
	l = [func(l1,l2)]
	l.extend(itr)
	return my_reduce(func,l)

def func(a,b):
	return a+b

itr = [1,2,3,4,5,6]
print(my_reduce(func,itr))
