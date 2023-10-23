import sys
list =[]

while(True):
 choice = int(input("Enter Your choice\n 1) Insertion Front\n 2Insertion Last\n 3)Insertion position\n 4) Display\n 5)Exit\n >>>  "))
 match choice:
    case 1:
        value = int(input("Enter the value to be inserted on front: "))
        list.insert(0,value)

    case 2:
        value = int(input("Enter the value to be inserted on last: "))
        list.append(value)

    case 3:
        pos = int(input("ENter the position: "))
        value = int(input("Enter the value to be inserted on position: "))
        list.insert((pos-1),value)

    case 4:
       print("List element are : ",list)

    case 5:
       sys.exit()

    case _:
        print("Enter the correct choice\n")
    