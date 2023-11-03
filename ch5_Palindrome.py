#palindrome program

s=r=0
n = int(input("Enter the number to check palindrome"))
while n!=0:
    d =n%10
    s = s+d
    r = (r*10) +d
    n = n//10

print(s)
print(r)
