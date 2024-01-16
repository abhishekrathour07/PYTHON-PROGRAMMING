list = [1, 2, 3, 4]
print(list)
#append() function
list.append(5)
print("Updated List : ",list)
#len () function
print("list length=",len(list))
# insert() function 
list.insert(0, 7)
print("New List: ",list)
#remove function
print("list after remove() fuction",list.remove(2))
print(list)
#pop function()
print("poping the element ",list.pop(0))
oldlist=print(list)
#clear() fuction
print("list after using clear() function")
newlist = list.clear()
print(newlist)
