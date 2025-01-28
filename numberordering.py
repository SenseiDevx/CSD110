def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Error: Enter a positive number")
        else:
            print("Error: Enter a positive integer.")


# Requesting 3 positive number from user
num1 = get_positive_integer("Enter a first integer: ")
num2 = get_positive_integer("Enter a second integer: ")
num3 = get_positive_integer("Enter a third integer: ")

# Sorting numbers without using sort(), min(), max() and lists
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

# Print the numbers in ascending order
print(f"Numbers in ascending order: {num1}, {num2}, {num3}")
