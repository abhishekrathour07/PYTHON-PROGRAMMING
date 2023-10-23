class employee:
    company_name = "Apple"
    def __init__(self,name) :
        self.name = name 
        self.sUp = 0.02
    def show(self):
        print(f"NAme of employee is {self.name} with {self.sUp} works in {self.company_name}")


e = employee("ABhishek")
e.company_name = "Google"
e.show()
e1 = employee("ABhishek")
e1.show()
