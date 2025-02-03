# Print 10x20 box of asterisks
for i in range(10):
    print("*" * 20)

print("\n")

# Print the asterisk arrow
for i in range(1, 10, 2):  # Increasing part
    print("*" * i)
for i in range(9, 0, -2):  # Decreasing part
    print("*" * i)
