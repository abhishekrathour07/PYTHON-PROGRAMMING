class overriden:
    def add (self,a,b):
        return a+b
class overriding(overriden):
    def add (self,a,b):
        return a*b
    
a = overriding()
value = a.add(10,3)
print(value)
a = overriden()
value = a.add(10,3)
print(value)