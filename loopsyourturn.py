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
