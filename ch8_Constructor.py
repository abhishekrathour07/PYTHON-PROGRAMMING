class emp:
    def __init__(self , id,name,salary) :
        self.id = id
        self.name =name
        self.salary = salary

    def display(self):
        print(f"id of employee is {self.id}")
        print(f"Name of employee is {self.name}")
        print(f"salary of employee is {self.salary}")


a = emp(101,"Abhishek",200000)
b = emp(102,"Rohit",300000)
a.display()
b.display()