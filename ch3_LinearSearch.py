n = int(input("Enter the number of element in list"))
list = []
c=0
for i in range(n):
   user_input = int(input("Enter an element: "))
   list.append(user_input)

print("Your list:", list)
search = int(input("Enter the element to be search : "))
for i in range(n):
   if(search==list[i]):
      print(f"Element is found at {i+1} position",)
      c=1
if c == 0 :
 print("Element is not found in the list")