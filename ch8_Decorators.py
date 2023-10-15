
def add(x, y):
    print("Performing addition operation ....")
    print("The values is ",(x+y))
    print("Adding operation done successfully")

def calculate(func, x, y):
    return func(x, y)

calculate(add, 4, 6)
