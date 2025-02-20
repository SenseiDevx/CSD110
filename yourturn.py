import random


def randomlyPopulateNumbers(filename):
    numbers_count = random.randint(50, 100)

    # Open the file for writing random numbers
    with open(filename, "w") as file:
        for i in range(numbers_count):
            numbers = random.randint(1, 1000)
            file.write(str(numbers) + "\n")


random.seed()
FILENAME = "numbers.txt"

randomlyPopulateNumbers(FILENAME)
