import sys
n = int(input("Enter the size of an list"))
list = []

for i in range(n):
    user_input = int(input("Enter the element in the list: "))
    list.append(user_input)
while(True):
 choice = int(input("Enter Your choice\n 1) Delete Front\n 2Delete Last\n 3)Delete position\n 4) Display\n 5)Exit\n >>>  "))
 match choice:
    case 1:
      print("Deleted Value are = ",list[0])
      list.remove(list[0])
    case 2: 
        print("Deleted value are ",list[(n-1)])
        list.pop()
    case 3:
         pos = int(input("ENter the position: "))
        #  list.pop(pos-1)-->Both will work
         del list[pos-1]
    case 4:
       print("LIst element are",list)
    case 5:
       sys.exit()
    