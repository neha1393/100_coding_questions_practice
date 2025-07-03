lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for i in range(lower, upper + 1):
    org = i
    n = len(str(i))
    sum = 0
    temp = i

    while temp > 0:
        last_dig = temp % 10
        sum += last_dig ** n
        temp = temp // 10

    if sum == org:
        print(org)
