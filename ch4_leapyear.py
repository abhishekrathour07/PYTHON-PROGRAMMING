year = int(input("Enter the year to check where the given number is prime or not : "))
if year%4==0 or year%400==0 and year%100!=0 :
    print("Prime number")
else :
    print("Not a prime number")    