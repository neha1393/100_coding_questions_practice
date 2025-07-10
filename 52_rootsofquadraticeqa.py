import math
a=int(input("enter coefficient a :"))
b=int(input("enter coefficient b :"))
c=int(input("enter coefficient c :"))
D=b*b-(4*a*c)
if a==0:
    print("the equation is not quadratic")
elif D>0:
    root1=((-b+D**0.5)/2*a)
    root2=((-b-D**0.5)/2*a)
    print(f'roots are {root1} and {root2}')
elif D==0:
    root=-b/2*a
    print("root is real and repeated ",root)
else:
    real=-b/2*a
    img=((-D)**0.5/2*a)
    print("complex roots : ")
    print(f'{real}+{img} and {real}-{img}')