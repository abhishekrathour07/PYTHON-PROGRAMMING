class Employee:
     __name = None
     __id= None
     __age = None
     def setdata(self ,id ,name,age):
        self.__id = id
        self.__name = name
        self.__age = age
        
     def getdata(self):
         print(f"The name of employee is {self.__name} with id {self.__id} and age is {self.__age}")

obj = Employee()
obj.setdata(101,"abhi",21)
obj.getdata()