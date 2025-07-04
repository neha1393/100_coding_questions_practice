n=int(input("enter the number of terms: "))
a,b=0,1
count=0
if n<=0:
    print('please enter a positive integer ')
elif (n==1):
    print("fibonacci series upto 1 term :")
    print(a)
else:
    print("fibonacci series ")
    while count<n:
        print(a,end=' ')
        a,b=b,a+b
        count+=1
