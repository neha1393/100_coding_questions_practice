number = int(input("Enter the number: "))
org = number
sum = 0

while number != 0:
    i = number % 10
    number = number // 10
    sum += i

if org % sum == 0:
    print(org, "is a Harshad number")
else:
    print(org, "is not a Harshad number")
