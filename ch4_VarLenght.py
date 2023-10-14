def name(*name):
    print("Top Three student is : ",name[0],name[1],name[2])

name("Abhishek","Rohit","Rahul")
def name1(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name1(mname = "Singh", lname = "Rathour", fname = "Abhishek")