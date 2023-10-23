class demo :
    def __init__(self,name):
        self.name = name 
        self.id =2

    def display(self):
        print("Hello ",self.name)

print(dir(list)) # get the method in the given class 
print(type(list))
print(help(demo))
print(demo.__dict__)