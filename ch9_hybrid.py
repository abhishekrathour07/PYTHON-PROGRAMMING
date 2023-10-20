class school:
    def func1(self):
        print("School is Here")

class student1(school):
     def func2(self):
        print("student1 is Here")
class student2(school):
     def func3(self):
        print("student2 is Here")
class student3(student1,student2):
     def func4(self):
        print("student3 is Here")

obj = student3()
obj.func1()
obj.func2()
