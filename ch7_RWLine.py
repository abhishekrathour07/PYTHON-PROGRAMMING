
f = open("file1.txt", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()


f = open("file1.txt","r")
for i in range(10):
 print(f.readline())

f.close()

