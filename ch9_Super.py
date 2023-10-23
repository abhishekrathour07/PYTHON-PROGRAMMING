class dept:

  def __init__(self,dpid, dname):
    self.dpid = dpid
    self.dname = dname 

  def display(self):
    print(f" Department id {self.dpid}\n Department name {self.dname}")


class Emp(dept):
   def __init__(self,dpid,dname,eid,ename,salary):
     super().__init__(dpid,dname)
     self.ename = ename 
     self.eid = eid
     self.salary = salary

   def dispay(self):
     super().display()
     print(f" Employee id = {self.eid}\n employee name = {self.ename}\n employee salary = {self.salary}")

obj = Emp(101,"Aigs","ags22","Abhishek",50000)
obj.dispay()


      
     
    