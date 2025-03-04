import random


def randomly_populate_numbers(filename):
    numbers_count = random.randint(50, 100)

    with open(filename, "w") as file:
        for _ in range(numbers_count):
            number = random.randint(1, 1000)
            file.write(f"{number}\n")


def read_numbers_from_number_txt(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                print("Debug line:", line)
                continue

    return numbers


def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    filename = "numbers.txt"

    randomly_populate_numbers(filename)

    numbers = read_numbers_from_number_txt(filename)
    average = compute_average(numbers)

    print(f"The average of the numbers in the file is {average:.2f}")


if __name__ == "__main__":
    main()
