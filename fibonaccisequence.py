def fibonacci_sequence(n):
    # Initial values of sequences
    a = 0
    b = 1
    print(a)  # First integer
    print(b)  # Second integer

    for _ in range(n):  # n times add numbers
        next_number = a + b
        print(next_number)
        # Updating values a и b
        a = b
        b = next_number


fibonacci_sequence(23)
