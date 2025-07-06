# Manual Decimal to Hexadecimal Conversion (no hex() used)

decimal = int(input("Enter a decimal number: "))
hex_digits = "0123456789ABCDEF"
hexadecimal = ""

if decimal == 0:
    hexadecimal = "0"
else:
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal = decimal // 16

print("Hexadecimal:", hexadecimal)
