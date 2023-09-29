
x = ['red','blue','green','orange',7,2.33]
print("performing basic operation\n")
print(x)
print(x[2])
print(x[2:5])

print("removing the last element from list\n")
print(x.pop())
print(x)

print("Inserting value in the list\n")
x.append(4)
print(x)

print("Removing element of particular index")
x.remove('orange')
print(x)

print("Inserting the multiple value\n")
x.insert(2,"abhi")
print(x)

print("getting the index of element\n")
print(x.index('green'))

# print("finding maximum value\n ")
# print(max(x)) --> support only there is  one type of value

del x  #--> deleting the whole list
print(x)





