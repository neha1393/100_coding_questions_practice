n = int(input("Enter the value of N: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Nth Fibonacci term is:", a)
elif n == 2:
    print("Nth Fibonacci term is:", b)
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Nth Fibonacci term is:", b)
