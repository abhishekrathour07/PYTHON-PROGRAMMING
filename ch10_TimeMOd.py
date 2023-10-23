import time

def whileloop():
    i =0
    while i<5000 :
        print(i)
        i =i+1

def forloop():
    for i in range(5000):
        print(i)

init = time.time()
whileloop()
t1 = time.time()- init

init = time.time()
forloop()
t2 = time.time()- init

print(t1)
print(t2)


