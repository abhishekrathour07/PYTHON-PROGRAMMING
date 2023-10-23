
n = int(input("Enter the size of an list"))
list = []

for i in range(n):
    user_input = int(input("Enter the element in the list"))
    list.append(user_input)
print("List element are:")
print(list)
print(" Sorted List element are:")
list.sort()
print(list)
search = int(input("Enter the element to be search"))
first = 0
last =n-1
while (first <= last):
     middle = (first + last) // 2
     
     if (list[middle] < search):
            first = middle + 1
     elif (list[middle] == search) :
         print(f"{search} found at location {middle + 1}" )
         break
     else :
      last = middle - 1
   
if (first > last):
 print(f"Not found! {search}  isn't present in the list.\n")
