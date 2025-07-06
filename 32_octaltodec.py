# Octal to Decimal Conversion

# Taking octal input from user
octal_input = input("Enter an octal number: ")

# Check if all digits are valid for octal (0-7)
if all(digit in '01234567' for digit in octal_input):
    decimal_output = int(octal_input, 8)
    print(f"The decimal value of octal {octal_input} is {decimal_output}")
else:
    print("Invalid input! Please enter a valid octal number (digits 0 to 7 only).")
