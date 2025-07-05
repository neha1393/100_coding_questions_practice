num=int(input("enter a number"))
org=num
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum>num:
    print(num,"is abundant number")
else:
    print(num,"is not an abundant number ")