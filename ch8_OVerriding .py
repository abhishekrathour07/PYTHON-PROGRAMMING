class a :
    def __init__(self,name) :
        self.name = name

    def about(self):
        print(f"the information is about the {self.name}")

class b:
    def __init__(self,address) :
        self.address= address
    
    def about(self):
        print(f"the address is {self.address}")

class c( b,a):
    def __init__(self, name, address, age):
        a.__init__(self, name)  # Call the __init__ of class 'a' explicitly
        b.__init__(self, address)  # Call the __init__ of class 'b' explicitly
        self.age = age

    def display(self):
        print(f"The name is {self.name}, age is {self.age}, and location is {self.address}")




obj = c('abhi','bangalore',21)
obj.display()
obj.about()
