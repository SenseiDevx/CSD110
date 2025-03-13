
def most_common_letter():
    string = input("Enter a string --> ")
    letter_counts = [0] * 26

    for char in string:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            letter_counts[index] += 1
        else:
            print(f"{char} is not an alphabetic character and will be ignored")

    max_count = max(letter_counts)

    if max_count == 0:
        print(f"{string} is not a valid string")
        return

    most_common = chr(letter_counts.index(max_count) + ord('a'))
    print(f"The most common letter in {string} is '{most_common}' occurring {max_count} times")

if __name__ == "__main__":
    most_common_letter()



