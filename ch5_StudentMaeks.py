a = int(input("Enter the marks in sub 1"))
b = int(input("Enter the marks in sub 2"))
c = int(input("Enter the marks in sub 3"))

total = a+b+c
per = float(total/3)
print(f"your per is {per} and you are fail") if(a<40 and b<40 and c<40 and per<40) else print(f"your per is {per} and your grade is c") if (per>=60) else print(f"your per is {per} and your grade is b") if(per>=80) else print(f"your per is {per} and your grade is a")
