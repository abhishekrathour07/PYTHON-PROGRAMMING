# import math
# factorial.l ----> We can also do like this
def fact(x):
    if(x==0 or x==1):
        return 1 
    else :
        return x * fact(x-1)
l = [2,3,4,5,6,6,8]
    
newl = list(map(fact,l))
square = lambda x : x*x
print(newl)

l1 = ["sad","Bad","Mad","Rat"]
test = list(map(list,l1))
print(test)
