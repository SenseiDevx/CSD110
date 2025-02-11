import random


def get_valid_guess_number(min_val, max_val, attempts_left):
    while True:
        print("You have", attempts_left, "guesses left")
        guess = input("Enter your guess between " + str(min_val) + " and " + str(max_val) + " --> ")
        if guess.isnumeric():
            guess = int(guess)
            if guess >= min_val and guess <= max_val:
                return guess
            else:
                print("Number not in range. Try again.")
        else:
            print("Invalid input. Enter a number.")


def play_guess_number_game():
    random.seed()
    mystery_num = random.randint(1, 10)
    min_guess = 1
    max_guess = 10
    attempts = 3

    while attempts > 0:
        print("Attempts left:", attempts)
        guess = get_valid_guess_number(min_guess, max_guess, attempts)

        if guess == mystery_num:
            print("You win! The number was:", mystery_num)
            return
        if guess < mystery_num:
            print("Too small!")
            min_guess = guess + 1
        if guess > mystery_num:
            print("Too large!")
            max_guess = guess - 1

        attempts = attempts - 1

    print("Game over! The number was:", mystery_num)


play_guess_number_game()
