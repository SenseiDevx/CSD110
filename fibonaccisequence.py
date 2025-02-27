def fibonacci_sequence(n):
    fibonacci_number_list = [0, 1]

    for i in range(n - 2):
        next_fibonacci_number = fibonacci_number_list[-1] + fibonacci_number_list[-2]
        fibonacci_number_list.append(next_fibonacci_number)

    return fibonacci_number_list


def main():
    n = 23
    fib_list = fibonacci_sequence(n)
    print(fib_list)


if __name__ == "__main__":
    main()
