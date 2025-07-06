# Binary to Octal in Python

binary = input("Enter a binary number: ")

try:
    decimal = int(binary, 2)        # Convert binary to decimal
    octal = oct(decimal)[2:]        # Convert decimal to octal
    print("Octal:", octal)
except ValueError:
    print("Invalid binary number!")

