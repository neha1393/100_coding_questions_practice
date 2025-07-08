def count_decodings(s, index=0):
    if index == len(s):
        return 1
    if s[index] == '0':
        return 0

    count = count_decodings(s, index + 1)

    if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
        count += count_decodings(s, index + 2)

    return count

# 💬 Take input from user
s = input("Enter a number string (like 226): ")

# Check if input is valid (non-empty and only digits)
if s and s.isdigit():
    result = count_decodings(s)
    print("Total decoding ways:", result)
else:
    print("Please enter a valid digit string (only numbers).")
