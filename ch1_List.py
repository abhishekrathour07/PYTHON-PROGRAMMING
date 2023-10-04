
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

print("Inserting the  value of given indexx\n")
x.insert(2,"abhi")
print(x)

print("getting the index of element\n")
print(x.index('green'))

# del x  #--> deleting the whole list
print(x)

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
print("performing sorting")
# y = [1,2,3,4,0,9] 
# print(y)
# # y.reverse()
# # y.sort()
# # y.sort(reverse=True)
x.extend(colors)

print(x)








