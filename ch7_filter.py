ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True



adults = filter(myFunc, ages)
l =[2,3,4,1,5,9,8]
newl1 = list(filter(lambda a : a%2==0,l))

print(newl1)
for x in adults:
  print(x)
