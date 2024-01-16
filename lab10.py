str=input("enter string : ")
f = {} 
for i in str: 
    if i in f: 
        f[i] += 1
    else: 
        f[i] = 1
print(f)
