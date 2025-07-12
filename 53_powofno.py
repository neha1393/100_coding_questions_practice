def powerofnum(base,exponent):
    if exponent==0:
        return 1
    else:
        return base*powerofnum(base,exponent-1)
base=int(input("enter a number "))
exponent=int(input("enter the power "))
print("The power of a number is ",powerofnum(base,exponent))





