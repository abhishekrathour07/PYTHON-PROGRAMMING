def fibo(n):
    if n ==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    

n = int(input("Enter the value to find the fibonacci"))

# for item in range(n+1):
#     print(fibo(item))
fib = [fibo(i) for i in range(n+1) ]
print(fib)
