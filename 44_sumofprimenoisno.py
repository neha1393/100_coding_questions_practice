# Get number from user
num = int(input("Enter a number: "))

found = False  # to check if any pair is found

# Try all numbers from 2 to num
for i in range(2, num):
    # check if i is prime
    prime1 = True
    for j in range(2, i):
        if i % j == 0:
            prime1 = False
            break

    # check if (num - i) is prime
    prime2 = True
    x = num - i
    for k in range(2, x):
        if x % k == 0:
            prime2 = False
            break

    # if both numbers are prime, print and stop
    if prime1 and prime2:
        print(num, "=", i, "+", x)
        found = True
        break

# if no prime pair found
if not found:
    print(num, "cannot be written as sum of two prime numbers")
