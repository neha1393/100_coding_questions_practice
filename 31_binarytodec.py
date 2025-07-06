binay_input=input("enter binary number ")
if all(bit in '01' for bit in binay_input):
    decimal_op=int(binay_input,2)
    print("the decimal number of ",binay_input,"is",decimal_op)
else:
    print("the input you have given is not binary no")