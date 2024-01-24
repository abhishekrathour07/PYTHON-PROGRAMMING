with open("lab11.py",'r') as file:
    data = file.read();
    f ={}
    for i in data:
        if i in f:
            f[i]+=1
        else:
            f[i] =1

print(data);
for i in f:
	print(i,":",f[i])
print(f)