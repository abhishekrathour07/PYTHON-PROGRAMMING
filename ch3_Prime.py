n = int(input("Enter the number to check prime: "))
c=0
if(n==0 or n==1):
  print(" Not a Prime Number ")
    
   
   
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(" Not a Prime Number ")
            c=1
            break
if(c==0):
 print("Prime number")