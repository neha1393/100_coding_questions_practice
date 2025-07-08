import math
def areaofcircle(r):
    if r>0:
        return math.pi * r * r
    else:
        return ("Enter valid radius")
r=int(input("enter radius of a circle "))
print("Area of circle is ",areaofcircle(r))