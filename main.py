import pygame
import pygame.surfarray as surfarray
import matplotlib.pyplot as plt
import random

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define some colors
colors = [(255, 125, 0), (0, 255, 125), (125, 0, 255), (255, 125, 0), (60, 0, 255), (0, 60, 255)]

# Set the number of circles to draw
num_circles = 500

# Generate the circles
circles = []
for i in range(num_circles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    radius = random.randint(8, 40)
    color = random.choice(colors)
    circles.append((x, y, radius, color))

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
