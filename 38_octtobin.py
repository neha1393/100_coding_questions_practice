# Octal to Binary in Python

octal = input("Enter an octal number: ")

try:
    decimal = int(octal, 8)          # Octal to decimal
    binary = bin(decimal)[2:]        # Decimal to binary
    print("Binary:", binary)
except ValueError:
    print("Invalid octal number!")
