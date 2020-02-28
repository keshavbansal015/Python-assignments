def longest_word(lis):
	len_of_words = list(map(len,lis))
	return len_of_words

str = 'Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass'.split()
print(longest_word(str))
