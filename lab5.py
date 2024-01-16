def add(a, b):
	return a+b
def sub(a, b):
	return a-b
def mul(a, b):
	return a*b
def div(a, b):
	return a/b
print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
choice = int(input(">>>"))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if choice==1:
	print("sum = ",add(a,b))
elif choice==2:
	print("Sub = ",sub(a,b))
elif choice==3:
	print("Mul = ",mul(a,b))
elif choice==4 :
	print("Div = ",div(a,b))
