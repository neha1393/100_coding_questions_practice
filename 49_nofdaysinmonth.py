month=int(input("enter a month number "))
if month<13 and month>0 :
    if month==2 :
        print("FEb has 28 or 29 days ")
    elif month in [1,3,5,7,8,10,12]:
        print("the month has 31days") 
    else:
        print("the month has 30 days ")   
else:
    print("enter valid month")