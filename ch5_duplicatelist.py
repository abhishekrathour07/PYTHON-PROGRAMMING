list =[]
n = int(input("Enter the size of an array"))
for i in range(n):
    element = int(input("Enter the element\n"))
    list.append(element)

print(list)

for i in range(n):
    for j in range(n-1):
        if(list[i]==list[j]):
            for k in range(n-1):
                list[k] = list[k+1]
    j = j-1
    n = n-1

print(list)
            









