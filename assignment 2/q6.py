def filter_long_words(lis,n):
	itr = [x for x in lis if len(x) > n]
	return itr

lis = 'Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass'.split()
n = 6
print(filter_long_words(lis,n))
