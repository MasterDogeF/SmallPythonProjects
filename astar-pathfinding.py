import pygame
import math

WIDTH = 300
screen = pygame.display.set_mode((WIDTH,WIDTH))
screen.fill((255,255,255))

class Cell():
    def __init__(self, h, g, totalCost, parent, isObstacle=False):
        self.h = h
        self.g = g
        self.totalCost = totalCost
        self.isObstacle = isObstacle
        self.parent = parent

grid = []

def create_grid():
    for x in range(8):
        column = []
        for y in range(8):
            column.append(Cell(0, 0, None))
        grid.append(column)

create_grid()

for cell in grid:
    if cell.pos[1] == 7:
        print(cell.isObstacle, end="\n")
    else:
        print(cell.isObstacle, end="")

def algorithm(start, destination):
   openList = [grid[start[0], start[1]]]
   closedList = []

   start.h = heuristic(start, destination)
   start.totalCost = start.g + start.h
   start.parent = None

   while openList:
      current = openList.pop()
      if current == destination:
         return 
      
      closedList.append(current)
      



def heuristic(pos1, pos2):
   x1, y1 = pos1
   x2, y2 = pos2
   return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

