def revofnum(n,rev=0):
    if n==0:
        return rev
    else:
        rev=rev*10+(n%10)
        return revofnum(n//10,rev)
n=int(input("enter a number "))
print("Reversed number is : ",revofnum(n))
    