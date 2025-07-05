n1=int(input("enter first number "))

n2=int(input("enter 2nd number "))

sum1=0
sum2=0
for i in range(1,n1+1):
    if n1%i==0:
        sum1+=i
for j in range(1,n2+1):
    if n2%j==0:
        sum2+=j
if (sum1/n1)==(sum2/n2):
    print("the number are friendly pair")
else:
    print("the numbers are not frndly pair")