# Slide 11: Count from 0 to 10 using a while loop
i = 0
while i <= 10:
    print(i)
    i += 1

print("\n")

# Slide 19: Print odd numbers less than 15 using continue and break
for num in range(50):
    if num % 2 == 0:
        continue
    if num >= 15:
        break
    print(num)

print("\n")

# Slide 27: Compute sums of even numbers 1 to 100
# Using a for loop, counting backwards
sum_even_for = 0
for num in range(100, 0, -1):
    if num % 2 == 0:
        sum_even_for += num
print(f"Sum of even numbers (for loop): {sum_even_for}")

# Using a while loop with augmented assignment
sum_even_while = 0
num = 100
while num >= 1:
    if num % 2 == 0:
        sum_even_while += num
    num -= 1
print(f"Sum of even numbers (while loop): {sum_even_while}")