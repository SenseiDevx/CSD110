import turtle


def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    print(f"Done with size {size}")


def main():
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.title("Drawing Shapes")

    # Draw multiple squares of different sizes
    sizes = [50, 100, 150, 200]
    for size in sizes:
        draw_square(size)
        turtle.penup()
        turtle.forward(size + 10)  # Move to the next position
        turtle.pendown()

    # Finish
    screen.mainloop()
    print("4 squares successfully drawn")


if __name__ == "__main__":
    main()
