number=input("enter the number ")
x=input("enter a number x")
count=0
for i in number:
    if i==x:
        count+=1
print("the number of times ",x,"repeats in a number is ",count)