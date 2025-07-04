n=int(input("enter a number "))
factors=[]
for x in range(1,n+1):
    if n%x==0:
        factors.append(x)
print(factors)