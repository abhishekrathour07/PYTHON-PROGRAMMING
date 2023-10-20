class a :
    def display(self):
      print("This is class A")

class b(a):
   def display(self):
      super().display()
      print("This is class b")
class c(b):
 def display(self):
      super().display()
      print("This is class c")

obj = c()
obj.display()