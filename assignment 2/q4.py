def longest_word(lis):
	len_of_words = list(map(len,lis))
	longest = max(len_of_words)
	l = list(filter(lambda x: len(x)==longest,lis))
	return l

str = 'Function to take the length of the sides of triangle from user should be defined in the parent class and function to the area should be defined in subclass'.split()
print(longest_word(str))
