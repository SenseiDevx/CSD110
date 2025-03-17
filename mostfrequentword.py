import re
from collections import Counter


# Function for creating a file if we don't have
def create_harry_txt_file():
    sample_text = """
    Harry was a brave wizard. Harry loved magic. The wizard world was full of mysteries.
    Harry had many friends, and his best friend was Ron. Ron was loyal and funny.
    The world of Hogwarts was magical. Harry, Ron, and Hermione were the best trio.
    """

    with open("Harry_Potter.txt", "w") as file:
        file.write(sample_text)


# Functon for reading file
def read_file():
    try:
        with open("Harry_Potter.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Creating test file...")
        create_harry_txt_file()
        with open("Harry_Potter.txt", "r") as file:
            return file.read()


# Function for clearing text
def clean_text_function(text):
    text = text.lower()
    return re.findall(r'\b\w+\b', text)


def main():
    text = read_file()
    words = clean_text_function(text)

    word_count = Counter(words)

    sorted_words = word_count.most_common()

    if len(sorted_words) >= 5:
        fifth_most_common_word = sorted_words[4]
        print(
            f"The fifth most common word is '{fifth_most_common_word[0]}' with {fifth_most_common_word[1]} occurrences.")
    else:
        print("The text contains fewer than five unique words.")


if __name__ == "__main__":
    main()
