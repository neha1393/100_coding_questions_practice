n = int(input("Enter the number of people: "))

# Using the handshake formula
handshakes = n * (n - 1) // 2

print("Maximum number of handshakes possible:", handshakes)
