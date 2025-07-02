n=int(input("enter the number "))
if n<=1:
    print(f"{n} is not a prime number ")
else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a prime number")
            break
        else :
            print(f"{n} is a prime number ")
            
def isprime(num):
    if num<=1:
        return "is not a prime number"
    else:
        for i in range(2,num):
            if num%i==0:
                return f"{num} is not a prime number"
                break
            else:
                return f"{num} is a prime number "
num=int(input("enter the number"))
print(isprime(num))