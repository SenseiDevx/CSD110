def mirrored_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(rows):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()

    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()


rows = 8
mirrored_triangle(rows)