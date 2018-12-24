# Import libraries
import pygame
from dataclasses import dataclass

resolution = 1000 # Set resolution
grid = 5 # Set grid to 5
abstand = resolution // grid
radius = (abstand - 20) // 2

pygame.init() # Initialize pygame

screen = pygame.display.set_mode([resolution, resolution]) # Set resolution for both x and y

matrix = [[0] * grid for i in range(grid)]

@dataclass
class rotor:
    x : int
    y : int
    speed : float
    horizontal : bool
    angle : float = 0

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), radius, 2) # Draw circle on hirizontal line

def setup():
    for n in range(grid):
        x = n * abstand + abstand // 2
        y = abstand // 2
        matrix[0][n] = rotor(x, y, 0.05 * n, True)
        matrix[n][0] = rotor(y, x, 0.05 * n, True)

def draw():
    for n in range(1, grid):
        matrix[0][n].show()
        matrix[n][0].show()

setup()

loop = True
while loop:
    for event in pygame.event.get(): # Look for events
        if event.type == pygame.QUIT: # If event is happening
            loop = False # Change loop from true to false to stop the while loop
    screen.fill((0, 0, 0))
    draw()
    pygame.display.flip()

pygame.quit()