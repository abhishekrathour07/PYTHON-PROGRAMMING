try:
    a =10
    b=0
    result = a//b
    
except ZeroDivisionError  :
    print("Division by zero is not possible")

else:
    print("Result = ",result)
    
finally:
    print("This block is always executed")