
x = {'name':'abhishek','age':22,"dept":'AIGS','year':2023}
Y = x.copy() #copy the dict item
print("\nPrinting all the element in the dict")
print(x)

print("\nGetting all the keys")
print(x.keys())

print("Getting all the values in the dict")
print(x.values())

print("\nprinting the values help of keys")
print(x['name'])
print(x['dept'])
print(x['age'])

print("\nAdding new Values:")
x['loc'] = "Bihar"
print(x)

print("\nDeleting the values")
x.pop('year')
print(x)

print("\ndelete the last value of list")
x.popitem()
print(x)
print(Y)




