def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

# Example usage:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = hcf(num1, num2)
print("HCF is:", result)
