import time

t = time.localtime()
time1 = time.strftime("%H:%M:%S", t)
h = int(time.strftime('%H'))
print(time1)

print(h)

if(h>=6 and h<=12):
    print("Good morning abhishek")
elif(h>12 and h<16):
    print("Good afternoon abhishek")
elif(h>16 and h<21):
    print("Good evening abhishek")
else :
    print("Good night abhishek")
