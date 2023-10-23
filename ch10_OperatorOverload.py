class A:
    def __init__(self, a):
        self.a = a
 
    def __add__(self, o):
        return self.a + o.a 
class A1:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(1)
ob2 = A(2)
ob3 = A("Abhishek")
ob4 = A(" Singh")
# by the help of these __add__ function we are able to do this 
print(ob1 + ob2)
print(ob3 + ob4)
				
ob1 = A1(2)
ob2 = A1(3)
print(ob1 < ob2)
ob3 = A1(3)
ob4 = A1(3)
print(ob3 == ob4)

