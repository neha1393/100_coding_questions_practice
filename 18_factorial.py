N=int(input("enter a number "))

if N<0: 
    print("factorial of negative numbers is not defined")
elif (N==0) or (N==1):
    print("factorial is 1")
else:
    fact=1
    for i in range(1,N+1):
        fact*=i
    print("factorial is",fact)
         
def factorial(n):
    if n<0:
        return("factorial not defined ")
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return("factorial is",fact)
N=int(input("enter the number "))
result=factorial(N)
print(result)