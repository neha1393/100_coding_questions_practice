n1=int(input("enter 1st number "))
n2=int(input("enter 2nd number"))
divofn1=[]
divofn2=[]
for i in range(1,n1+1):
    if n1%i==0:
        divofn1.append(i)
for j in range(1,n2+1):
    if n2%j==0:
        divofn2.append(j)
comonfactors=list(set(divofn1)&set(divofn2))
gcd=max(comonfactors)
print("the gcd is: ",gcd)