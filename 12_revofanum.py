number=int(input("enter a number "))
rev=0
while number>0:
    last_dig=number%10
    rev=rev*10+last_dig
    number=number//10
print(rev)