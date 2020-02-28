import string
l = ['x','y','z']


l1 = list(string.ascii_uppercase)
print([l1[x] for x in range(0,20)])

l2 = []
print([y*_ for y in [x for x in l] for _ in range(1,5)])


l3 = [x*_ for _ in range(1,5) for x in l]
print(l3)


l4 = []
[l4.extend(y) for y in [[[x],[x+1],[x+2]] for x in range(2,5)]]
print(l4)


l5 = [[x,x+1,x+2,x+3] for x in range(2,6)]
print(l5)


l6 = [(y,x) for x in range(1,4) for y in range(1,4)]
print(l6)
