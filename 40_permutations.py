n = int(input("Enter the number of people (n): "))
r = int(input("Enter the number of seats (r): "))

if r > n:
    print("Seats cannot be more than people!")
else:
    numerator = 1
    for i in range(1, n + 1):
        numerator *= i

    denominator = 1
    for j in range(1, n - r + 1):
        denominator *= j

    permutation = numerator // denominator
    print(f"Number of ways: {permutation}")
