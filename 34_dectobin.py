# Decimal to Binary Conversion

decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # bin() converts to binary, [2:] removes '0b'
print("Binary:", binary)
