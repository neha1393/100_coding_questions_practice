def len_of_str(s):
    if s=="":
        return 0
    else:
        return 1+len_of_str(s[1:])
string1=input("enter a string")
print("Length of a string is : ",len_of_str(string1))