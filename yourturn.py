import random


def randomlyPopulateNumbers(filename):
    numbers_count = random.randint(50, 100)

    with open(filename, "w") as file:
        for _ in range(numbers_count):
            number = random.randint(1, 1000)
            file.write(f"{number}\n")


def computeSumofNumbersInFile(filename):
    total_sum = 0

    with open(filename, "r") as file:
        for line in file:
            try:
                number = int(line.strip())
                total_sum += number
            except ValueError:
                print("Debug line:", line)
                continue
    return total_sum


def appendSum(filename, sum):
    with open(filename, "a") as file:
        file.write(f"{sum}\n")


filename = "numbers.txt"

randomlyPopulateNumbers(filename)

total_sum = computeSumofNumbersInFile(filename)
print(f"The sum of the numbers in the file is {total_sum}.")

appendSum(filename, total_sum)
