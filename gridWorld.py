import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (119, 161, 203)

# Sets the WIDTH and HEIGHT of each block
WIDTH = 74
HEIGHT = 74

# This sets the margin between cells
MARGIN = 5

# Create a 2 dimensional array.
grid = []
for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(5):
        grid[row].append(0)  # Append a cell

#set pickup
grid[0][0] = 1
grid[2][2] = 1
grid[4][4] = 1

#set drop off
grid[1][4] = 2
grid[4][0] = 2
grid[4][2] = 2

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title
pygame.display.set_caption("AI GROUP PROJECT ANIMATION")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 4
            #print("Click ", pos, "Grid coordinates: ", row, column)
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(5):
        for column in range(5):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            if grid[row][column] == 2:
                color = RED
            if grid[row][column] == 3:
                color = BLACK
            if grid[row][column] == 4:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # update screen with drawing
    pygame.display.flip()

# Quit
pygame.quit()