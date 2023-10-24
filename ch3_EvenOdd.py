list = []
n = int(input("Enter the size of the list"))

for i in range(n):
    user_input = int(input(f"Enter the element in {i} index"))
    list.append(user_input)
print("Even no in list is :")
for i in range(n):
    if list[i]%2 ==0:
        print(list[i])
print("odd no in list is :")
for i in range(n):
    if list[i]%2 !=0:
        print(list[i])