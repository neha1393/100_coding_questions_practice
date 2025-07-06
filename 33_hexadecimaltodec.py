hex_input = input("Enter a hexadecimal number: ")

try:
    decimal_output = int(hex_input, 16)
    print(f"The decimal value of hexadecimal {hex_input.upper()} is {decimal_output}")
except ValueError:
    print("Invalid input! Please enter a valid hexadecimal number (0-9 and A-F only).")
