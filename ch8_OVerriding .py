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

class c(a,b):
    def __init__(self, name ,address, age):
        super().__init__(name)
        super.__init__(address)
        self.age= age
    def display(self):
     print(f"The name is {self.name} and age is {self.age} and loaction is {self.address}")


obj = c('abhi','bangalore',21)
obj.display()
obj.about()
