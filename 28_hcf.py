n1=int(input("enter 1st number"))
n2=int(input("enter 2nd numner"))
divisorofn1=[]
divisorofn2=[]
for i in range(1,n1+1):
    if n1%i==0:
        divisorofn1.append(i)
for j in range(1,n2+1):
    if n2%j==0:
        divisorofn2.append(j)
commondiv=list(set(divisorofn1)&set(divisorofn2))
hcf=max(commondiv)
print(hcf,"is the common factor")
