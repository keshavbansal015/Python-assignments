import numpy as np

def vandermonde(arr,N):
	return np.column_stack([arr**(i) for i in range(N)])

v = [3,4,5,7,6]
# ls = map(int,input().split())
# v = ls

arr = np.array(v)
count = arr.size
# Using numpy function
# print(np.vander(arr, increasing=True))

print(vandermonde(arr, count))
