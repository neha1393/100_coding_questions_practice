number=int(input("enter a number "))
org=number
n=len(str(number))
sum=0
while number>0:
    last_dig=number%10
    sum+=last_dig**n
    number=number//10
if sum==org:
    print("number is an armstrong ")
else:
    print("number is not an armstrong")    
    
    