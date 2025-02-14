import turtle

BRICK_WIDTH = 60
BRICK_HEIGHT = 30


def init_turtle():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.pendown()


# Function for drawing a rectangle with specified width and height
def draw_a_rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


# Function for draw a square
def draw_a_square(size):
    draw_a_rectangle(size, size)


# Function for drawing a single horizontal row of rectangular bricks
def draw_row(num_bricks):
    for i in range(num_bricks):
        draw_a_rectangle(BRICK_WIDTH, BRICK_HEIGHT)
        turtle.forward(BRICK_WIDTH)
    turtle.backward(num_bricks * BRICK_WIDTH)


# Function to draw a row of bricks with an offset
def draw_offset_row(num_bricks):
    turtle.forward(BRICK_WIDTH / 2)
    for i in range(num_bricks - 1):
        draw_a_rectangle(BRICK_WIDTH, BRICK_HEIGHT)
        turtle.forward(BRICK_WIDTH)
    draw_a_square(BRICK_HEIGHT)
    turtle.backward((num_bricks - 1) * BRICK_WIDTH + BRICK_WIDTH // 2)


# The main function that controls the process of drawing a wall of bricks
def main():
    init_turtle()
    num_rows = 20
    num_bricks_per_row = 9

    for i in range(num_rows):
        if i % 2 == 0:  # If the row is even (0, 2, 4...), draw an even row of bricks
            draw_row(num_bricks_per_row)
        else:  # If the row is odd (1, 3, 5...), draw an offset row
            draw_offset_row(num_bricks_per_row)
        turtle.right(90)
        turtle.forward(BRICK_HEIGHT)
        turtle.left(90)

    turtle.done()


main()
