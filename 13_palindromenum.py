n=int(input("entrer the number "))
org=n
rev=0
while n>0:
    last_dig=n%10
    rev=rev*10+last_dig
    n=n//10
if org==rev:
    print(org,"is a palindrome")
else:
    print(org,"is not a palindrome ")