class addsub:

    def __init__(self,x,y) :
         self.n1 = x
         self.n2 = y
    
    def add(self):
        return self.n1+self.n2
    
    def sub(self):
        return self.n1-self.n2
    
class muldiv(addsub):
    def __init__(self,x,y):
         super().__init__(x,y)

    def mul(self):
        return self.n1 * self.n2
    
    def div(self):
        return self.n1 /self.n2

x = int(input("Enter the first value"))
y = int(input("Enter the second value"))
obj = muldiv(x,y)
print("Addition = ",obj.add())
print("Subtraction = ",obj.sub())
print("Multiply = ",obj.mul())
print("Division =",obj.div())