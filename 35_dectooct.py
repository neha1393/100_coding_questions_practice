# Manual Decimal to Octal Conversion (No oct() used)

decimal = int(input("Enter a decimal number: "))
octal = ""

if decimal == 0:
    octal = "0"
else:
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8

print("Octal:", octal)
