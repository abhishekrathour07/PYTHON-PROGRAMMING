# def add(a,b):
#     return a+b
# r = add(22,8)
# print(r)---->we can also write this using lambda function

double = lambda x : x*2
cube = lambda x : x*x*x
EvenOdd = lambda x : 'Even Number' if x%2 ==0 else 'Odd Number'
big  = lambda x,y,z : f'{x} is bigger' if x>y and y>z else f'{y} is bigger' if y>x and y>z else f'{z} is geater'
print(big(344,564,123))
print(EvenOdd(4))
print(double(3))
print(cube(3))

