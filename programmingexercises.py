# 1
def display_numbers(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


display_numbers("numbers.txt")


# 2
def display_five_lines():
    filename = input("Enter the file name: ")

    try:
        with open(filename, 'r') as file:
            for i in range(5):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


display_five_lines()

# 3
def display_file_with_line_numbers():
    filename = input("Enter the file name: ")

    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"{line_number}: {line}", end='')
                line_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


display_file_with_line_numbers()
