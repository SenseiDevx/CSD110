import pygame
import sys

# Color Named Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constants
LINE_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 4
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Globals
screen = None
winner = None
turn = RED

grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def main():
    gameLoop()


def processGridClick(row, column):
    global turn, grid

    if row != 0:
        return

    for r in range(BOARD_SIZE - 1, -1, -1):
        if grid[r][column] is None:
            grid[r][column] = turn
            animate_circle(r, column, turn)
            turn = GREEN if turn == RED else RED
            return


def check_for_winner():
    global winner

    # Check for horizontal
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE - 3):
            if grid[row][col] is not None:
                if grid[row][col] == grid[row][col + 1]:
                    if grid[row][col] == grid[row][col + 2]:
                        if grid[row][col] == grid[row][col + 3]:
                            winner = grid[row][col]
                            return

    # Check for vertical
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE - 3):
            if grid[row][col] is not None:
                if grid[row][col] == grid[row + 1][col]:
                    if grid[row][col] == grid[row + 2][col]:
                        if grid[row][col] == grid[row + 3][col]:
                            winner = grid[row][col]
                            return

    # Check for diagonal left top to right bottom
    for row in range(BOARD_SIZE - 3):
        for col in range(BOARD_SIZE - 3):
            if grid[row][col] is not None:
                if grid[row][col] == grid[row + 1][col + 1]:
                    if grid[row][col] == grid[row + 2][col + 2]:
                        if grid[row][col] == grid[row + 3][col + 3]:
                            winner = grid[row][col]
                            return

            # Check for diagonal right top to left bottom
            if grid[row][col + 3] is not None:
                if grid[row][col + 3] == grid[row + 1][col + 2]:
                    if grid[row][col + 3] == grid[row + 2][col + 1]:
                        if grid[row][col + 3] == grid[row + 3][col]:
                            winner = grid[row][col + 3]
                            return

    # Check for tie
    is_full = True
    for row in grid:
        for cell in row:
            if cell is None:
                is_full = False
                break
        if not is_full:
            break

    if is_full:
        winner = "Tie Game"


def animate_circle(final_row, col, color):
    global screen

    # Анимация падения круга по одному шагу
    for r in range(final_row + 1):
        draw_circle(r, col, color)      # Рисуем круг на текущем уровне
        pygame.display.flip()          # Обновляем экран
        pygame.time.delay(100)         # Плавность анимации
        if r != final_row:             # Стираем круг на предыдущей позиции
            draw_circle(r, col, BLACK)


def Init():
    global screen
    pygame.init()

    # Initialize the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect Four")

    # Draw the grid
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)


def draw_circle(row, col, color):
    global screen
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.circle(screen, color, (x, y), SQUARE_SIZE // 2.25)


def gameLoop():
    Init()

    while winner is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                processGridClick(clicked_row, clicked_col)
                check_for_winner()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

    if winner == RED:
        input("RED won! Press enter to exit")
    elif winner == GREEN:
        input("GREEN won! Press enter to exit")
    elif winner != None:
        input("Tie game! Press enter to exit")


if __name__ == "__main__":
    main()