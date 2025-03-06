user_input = input("Enter the number ---->")

numbers = user_input.split(',')

binary_list = []

for i in numbers:
    num = i.strip()
    if num.isdigit():
        binary_list.append(0 if int(num) % 2 == 0 else 1)

print(binary_list)