i = 1
while (i<5):
    pass

for j in range(5):
    pass

if (i == 2):
    pass
list =[1,2,3,4,5,6,]
print(sum(list))

from functools import reduce
square = lambda x : x*x
l = [2,3,4,5,6,7,8,9,8,9,0]
newl = list(map(square,l))
print(newl)
newl1 = list(filter(lambda a : a>3,l))
print(newl1)
l1 = [2,2,2,2,2,2,2,2,2,2]
newl2 = reduce(lambda a,b: (a*b),l1)
print(newl2)
