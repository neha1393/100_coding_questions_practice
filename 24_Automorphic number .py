number = int(input("Enter a number: "))
sqrno = number * number

# Get number of digits in the original number
num_digits = len(str(number))
# Get the last digits from the square
last_digits = sqrno % (10 ** num_digits)

if last_digits == number:
    print("The number is an Automorphic Number.")
else:
    print("The number is NOT an Automorphic Number.")
