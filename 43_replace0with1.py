num = int(input("Enter an integer: "))

# Convert to string and replace 0 with 1
new_num = str(num).replace('0', '1')

# Convert back to integer if needed
new_num = int(new_num)

print("Number after replacing 0 with 1:", new_num)
