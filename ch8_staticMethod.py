class student:
    
    @staticmethod
    def staticAdd(x,y):
        return x+y
    
    def add(self,x,y):
        return x+y
    

obj = student()

print(student.staticAdd(3,4))
print(obj.add(4,5))
