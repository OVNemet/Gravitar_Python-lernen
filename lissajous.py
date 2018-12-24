# Import libraries
import pygame
import math
from dataclasses import dataclass

resolution = 1000 # Set resolution
grids = 10 # Set grid to 5
abstand = resolution // grids
radius = (abstand - 20) // 2

pygame.init() # Initialize pygame

screen = pygame.display.set_mode([resolution, resolution]) # Set resolution for both x and y

matrix = [[0] * grids for i in range(grids)]

@dataclass
class rotor:
    x : int
    y : int
    speed : float
    horizontal : bool
    angle : float = 0
    dotX : int = 0
    dotY : int = 0

    def show(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), radius, 1) # Draw circle on hirizontal line
        pygame.draw.circle(screen, (255, 255, 255), (self.dotX, self.dotY), 3, 3) # Draw circle on hirizontal line
        if self.horizontal:
            pygame.draw.line(screen, (50, 50, 50), (self.dotX, self.dotY), (self.dotX, resolution))
        else:
            pygame.draw.line(screen, (50, 50, 50), (self.dotX, self.dotY), (resolution, self.dotY))


    def update(self):
        self.angle += self.speed
        self.dotX = int(self.x + radius * math.cos(self.angle))
        self.dotY = int(self.y + radius * math.sin(self.angle))

@dataclass
class Lissajous:
    vertices: list

    def update(self, position):
        self.vertices.append(position)

    def show(self):
        if len(self.vertices) > 1:
            pygame.draw.lines(screen, (255, 0, 0), False, self.vertices, 1)



def setup():
    for n in range(grids):
        x = n * abstand + abstand // 2
        y = abstand // 2
        matrix[0][n] = rotor(x, y, 0.05 * n, True)
        matrix[n][0] = rotor(y, x, 0.05 * n, False)
    for row in range(1, grids):
        for grid in range(1, grids):
            matrix[row][grid] = Lissajous([])

def draw():
    for n in range(1, grids):
        matrix[0][n].update()
        matrix[n][0].update()
        matrix[0][n].show()
        matrix[n][0].show()

setup()

loop = True
clock = pygame.time.Clock()

while loop:
    clock.tick(20)
    for event in pygame.event.get(): # Look for events
        if event.type == pygame.QUIT: # If event is happening
            loop = False # Change loop from true to false to stop the while loop
    screen.fill((0, 0, 0))
    draw()
    pygame.display.flip()

pygame.quit()