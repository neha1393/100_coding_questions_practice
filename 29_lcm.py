def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_hcf(a, b)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("LCM is:", find_lcm(n1, n2))
