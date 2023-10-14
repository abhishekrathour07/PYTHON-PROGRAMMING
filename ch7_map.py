# def fact(x):
#     if(x==0 or x==1):
#         return 1 
#     else :
#         return x * fact(x-1)
import math
l = [2,3,4,5,6,6,8]

square = lambda x : x*x
newl = list(map(math.factorial,l))
print(newl)

l1 = ["sad","Bad","Mad","Rat"]
test = list(map(list,l1))
print(test)
