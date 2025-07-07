# Take inputs
num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))

# Step 1: Cross-multiply and add
numerator = (num1 * den2) + (num2 * den1)

# Step 2: Multiply the denominators
denominator = den1 * den2

# Step 3: Show the result (unsimplified)
print("Sum of the fractions is:", numerator, "/", denominator)
