class a :
    def func1(self):
        print("Hello A")

class b(a):
    def func2(self):
        print("Hello  b")

class c(a):
    def func3(self):
        print("Hello c")

obj = c()
obj.func1()
# obj.func2()
obj.func3()
