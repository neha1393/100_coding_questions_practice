N=int(input("enter a number "))
x=int(input("enter a number of divisors you want "))
count_of_no=0
for i in range(1,N+1):
    divisor_count=0
    for j in range(1,i+1):
        if i%j==0:
            divisor_count+=1
    if divisor_count==x:
        count_of_no+=1
print("number of intergers with exactly",x,"divisors is",count_of_no)
            