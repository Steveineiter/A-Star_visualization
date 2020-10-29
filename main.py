try:
    import pygame
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
except:
    pass

# Game field
WIDTH, HEIGHT = (900, 900)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (148, 62, 143)

# Utility
NUMBER_OF_ROWS = 30
NUMBER_OF_COLUMNS = 30
PIXEL_PER_BOX_WIDTH = WIDTH / NUMBER_OF_ROWS
PIXEL_PER_BOX_HEIGHT = HEIGHT / NUMBER_OF_COLUMNS
BOX_SIZE = 3

# TODO poder if we need this
grid = []
# Mit pygame machen wir die visualisieriung mit tkinter die eingabe usw


def start_up():
    # Creating 2D Array
    global grid
    grid = [[0 for i in range(NUMBER_OF_ROWS)] for j in range(NUMBER_OF_COLUMNS)]  # same as the next few lines

    # Creating Spots
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_COLUMNS):
            grid[i][j] = BoxInGrid(i, j)

    # Set start and end node
    start = grid[5][5]
    end = grid[NUMBER_OF_ROWS - 6][NUMBER_OF_COLUMNS - 6]

    start.color = end.color = PURPLE
    start.is_changeable = end.is_changeable = False


def add_box_neighbor():
    pass


class BoxInGrid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = WHITE
        self.is_blocked = False
        self.is_changeable = True

    def draw(self, window, box_with):
        pygame.draw.rect(window, self.color, (self.x * PIXEL_PER_BOX_WIDTH, self.y * PIXEL_PER_BOX_HEIGHT, 10, 10), box_with)


def redraw_window():
    # print(grid)
    for row in grid:
        for box in row:
            box.draw(WINDOW, BOX_SIZE)

    pygame.display.update()


def handle_mouse_press(mouse_position):
    x_axis, y_axis = mouse_position
    x_pos = x_axis // PIXEL_PER_BOX_WIDTH
    y_pos = y_axis // PIXEL_PER_BOX_HEIGHT

    access_point = grid[int(x_pos)][int(y_pos)]
    if not access_point.is_blocked and access_point.is_changeable:
        access_point.color = BLUE
        access_point.is_blocked = True


if __name__ == '__main__':
    run = True
    fps = 60
    clock = pygame.time.Clock()

    start_up()
    box_in_grid = BoxInGrid(100, 100)

    while(run):
        clock.tick(fps)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                mouse_position = pygame.mouse.get_pos()
                handle_mouse_press(mouse_position)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                print("yes your majesti")
                run = False

    add_box_neighbor()

