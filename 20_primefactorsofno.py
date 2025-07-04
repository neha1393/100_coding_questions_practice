n = int(input("Enter a number: "))
factors = []
primefactors = []

# Step 1: Find all factors
for x in range(1, n + 1):
    if n % x == 0:
        factors.append(x)

# Step 2: Check which of the factors are prime
for i in factors:
    if i > 1:  # ignore 1
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            primefactors.append(i)

print("Prime factors are:", primefactors)
