import math

def is_strong_number(num):
    total = 0
    for digit in str(num):
        total += math.factorial(int(digit))
    return total == num

# Example usage
num = int(input("Enter a number: "))
if is_strong_number(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is NOT a Strong Number.")
