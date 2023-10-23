from datetime import date

class  person:
    def __init__(self,name,age) :
        self.name = name
        self.age =age

    @classmethod
    def birthdate(cls,name,bdate):
        return cls(name,date.today().year - bdate)
    
    def display(self):
        print(self.name ," ",str(self.age))


p = person("Abhi",21)
p2 = person.birthdate("jai",2002)
p.display()
p2.display()

class Person1:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person1('mayank', 21)
person2 = Person1.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age) 

# print the result
print(Person1.isAdult(22))
