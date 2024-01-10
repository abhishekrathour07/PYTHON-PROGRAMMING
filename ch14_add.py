a=20
b=30
while b!=0:
    temp=a&b
    a=a^b
    b=temp<<1

print(a)