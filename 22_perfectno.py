num=int(input("enter a number "))
orginalno=num
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if orginalno==sum:
    print(num,"is a perfect number ")
else:
    print(num,'is not a perfect number ')
    