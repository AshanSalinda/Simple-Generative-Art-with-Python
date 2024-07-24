import pygame
import pygame.surfarray as surfarray
import matplotlib.pyplot as plt
import random

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the size of the grid
grid_size = 120

# Calculate the size of a cell in the grid
cell_size = screen_width // grid_size

# Calculate the radius of colors
radius = cell_size // 2 + 1

# Define some colors
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (255, 255, 0)]

# select a color randomly
r, g, b = random.choice(colors)

# Select a pattern randomly
selector = random.choice([1, 2, 3])

# Generate the circles
circles = []

# pattern 1
if selector == 1:
    circles.append((cell_size // 2, cell_size // 2, cell_size // 2 + 1, (r, g, b)))
    for n in range(1, grid_size):
        for m in range(n, grid_size):
            if n == 1:
                # middle
                xIndex = m * cell_size + cell_size // 2
                circles.append((xIndex, xIndex, radius, (r, g, b)))

            # first harf
            xIndex = m * cell_size + cell_size // 2
            yIndex = (m-n) * cell_size + cell_size // 2
            circles.append((xIndex, yIndex, radius, (r, g, b)))

            # second harf
            xIndex = (m - n) * cell_size + cell_size // 2
            yIndex = m * cell_size + cell_size // 2
            circles.append((xIndex, yIndex, radius, (r, g, b)))


        # change color to next
        if (r != 0 and g == 0) or (g == 0 and b == 0):
            if b < 205:
                b += 51
            elif b == 255:
                if r > 50:
                    r -= 51
        if (b != 0 and r == 0) or (r == 0 and g == 0):
            if g < 205:
                g += 51
            elif g == 255:
                if b > 50:
                    b -= 51
        if (g != 0 and b == 0) or (r == 0 and b == 0):
            if r < 205:
                r += 51
            elif r == 255:
                if g > 50:
                    g -= 51

else:
    for n in range(grid_size // 2):
        # pattern 2
        if selector == 2:
            # top-left part
            for topLeft in range(n + 1):
                xIndex = n * cell_size + cell_size // 2
                yIndex = topLeft * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))
                if topLeft != n:
                    xIndex = topLeft * cell_size + cell_size // 2
                    yIndex = n * cell_size + cell_size // 2
                    circles.append((xIndex, yIndex, radius, (r, g, b)))

            # top-right part
            for topRight in range(n + 1):
                xIndex = n * cell_size + cell_size // 2
                yIndex = (grid_size - (topRight + 1)) * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))
                if topRight != n:
                    xIndex = topRight * cell_size + cell_size // 2
                    yIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                    circles.append((xIndex, yIndex, radius, (r, g, b)))

            # bottom-left part
            for bottomLeft in range(n + 1):
                xIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                yIndex = bottomLeft * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))
                if bottomLeft != n:
                    xIndex = (grid_size - (bottomLeft + 1)) * cell_size + cell_size // 2
                    yIndex = n * cell_size + cell_size // 2
                    circles.append((xIndex, yIndex, radius, (r, g, b)))

            # top-right part
            for bottomLeft in range(n + 1):
                xIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                yIndex = (grid_size - (bottomLeft + 1)) * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))
                if bottomLeft != n:
                    xIndex = (grid_size - (bottomLeft + 1)) * cell_size + cell_size // 2
                    yIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                    circles.append((xIndex, yIndex, radius, (r, g, b)))

        # pattern 3
        if selector == 3:
            # top part
            for top in range(n, grid_size - n):
                xIndex = n * cell_size + cell_size // 2
                yIndex = top * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))

            # left part
            for left in range(n + 1, grid_size - n):
                xIndex = left * cell_size + cell_size // 2
                yIndex = n * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))

            # bottom part
            for bottom in range(n + 1, (grid_size - n)):
                xIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                yIndex = (grid_size - bottom) * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))

            # right part
            for right in range(n + 1, grid_size - (n + 1)):
                xIndex = (grid_size - (right + 1)) * cell_size + cell_size // 2
                yIndex = (grid_size - (n + 1)) * cell_size + cell_size // 2
                circles.append((xIndex, yIndex, radius, (r, g, b)))

        # change color to next
        if (r != 0 and g == 0) or (g == 0 and b == 0):
            if b < 205:
                b += 51
            elif b == 255:
                if r > 50:
                    r -= 51
        if (b != 0 and r == 0) or (r == 0 and g == 0):
            if g < 205:
                g += 51
            elif g == 255:
                if b > 50:
                    b -= 51
        if (g != 0 and b == 0) or (r == 0 and b == 0):
            if r < 205:
                r += 51
            elif r == 255:
                if g > 50:
                    g -= 51


# Draw the circles
for circle in circles:
    pygame.draw.circle(screen, circle[3], (circle[0], circle[1]), circle[2])

# Convert the Pygame surface to a NumPy array
pygame.display.flip()
pygame.surfarray.use_arraytype("numpy")
image = surfarray.array3d(screen)

# Display the image using Matplotlib
plt.imshow(image)
plt.axis("off")
plt.show()

# Quit Pygame
pygame.quit()
