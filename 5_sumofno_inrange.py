def sum_in_range(a,b):
    totalsum=0
    for i in range(a,b+1):
        totalsum+=i
    return totalsum
a=int(input("enter the first number "))
b=int(input("enter the last number "))

print("the sum of the given range of numbers is ",sum_in_range(a,b))