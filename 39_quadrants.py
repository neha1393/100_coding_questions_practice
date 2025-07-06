x=float(input("enter the number x"))
y=float(input("enter the number y"))
if (x,y)==(0,0):
    print("the coodinates lie on the origin ")
elif (x==0)and (y!=0):
    print("the cordinate lies on y axis")
elif (x!=0) and (y==0):
    print("the coordinates lies on x axis ")
elif (x>0) and (y>0):
    print("its I quadrant")
elif (x<0) and (y>0):
    print("its II quadrant")
elif (x<0) and (y<0):
    print("its III quadrant")
elif (x>0) and (y<0):
    print("its IV quadrant")