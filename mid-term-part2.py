import turtle

SQUARE_SIZE = 30
ROWS = 4
COLS = 16


def draw_black_square(xPosition, yPosition, size):
    """Draws a filled black square at the given position."""
    turtle.penup()
    turtle.goto(xPosition, yPosition)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def draw_checked_row(start_x, start_y, number_of_cols, square_size, offset=False):
    for column in range(number_of_cols):
        x = start_x + column * square_size
        y = start_y
        if (column + offset) % 2 == 0:
            draw_black_square(x, y, square_size)


def draw_checked_flag(rows, cols, square_size):
    start_x = -cols * square_size / 2
    start_y = rows * square_size / 2

    for row in range(rows):
        y = start_y - row * square_size
        draw_checked_row(start_x, y, cols, square_size, offset=row % 2)


def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.fillcolor("black")

    draw_checked_flag(ROWS, COLS, SQUARE_SIZE)

    turtle.done()


main()
