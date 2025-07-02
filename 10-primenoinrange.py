x=int(input("enter the start"))
y=int(input("enter the end "))
for i in range(x, y+1):
        if i<=1:
            print(f"{i} is not a prime number")
            continue
        for j in range(2,i): 
            if i%j==0:
                   print(f"{i} is not a prime number")
                   break
        else:
                   print(f"{i} is a prime number ")
                   
