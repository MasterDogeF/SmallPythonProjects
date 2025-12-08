import math
import random
from rich.console import Console
from enum import Enum

WIDTH = 300
grid_size = 32

class Node():
    def __init__(self, pos, isObstacle=False):
        self.pos = pos
        self.h = 0
        self.g = math.inf
        self.totalCost = 0
        self.isObstacle = isObstacle
        self.isPath = False
        self.parent = None
        self.checked = False

grid = []

def add_obstacles(amount, start, destination):
    placed = 0
    while placed < amount:
        x = random.randint(0,grid_size-1)
        y = random.randint(0,grid_size-1)

        if grid[x][y] != start and grid[x][y] != destination and not grid[x][y].isObstacle:
            grid[x][y].isObstacle = True
            placed += 1

def create_grid():
    for x in range(grid_size):
        column = []
        for y in range(grid_size):
            column.append(Node((x,y)))
        grid.append(column)

def algorithm(start, destination):
    openList = [start] #nodes that are discovered but may still be able to find a cheaper path to them,
    closedList = [] #final nodes

    start.g = 0
    start.h = heuristic(start.pos, destination.pos)
    start.totalCost = start.g + start.h
    start.parent = None

    while openList: # openlist is not empty
        
        # find node in openlist with lowest cost
        current = openList[0]
        for node in openList:
            if node.totalCost < current.totalCost:
                current = node

        openList.remove(current)

        if current == destination:
            return make_path(start, destination)
        
        closedList.append(current)
    
        for neighbor in get_neighbors(current.pos):
            if neighbor in closedList:
                continue

            tentative_g = current.g + heuristic(current.pos, neighbor.pos)

            if neighbor not in openList:
                openList.append(neighbor)
                neighbor.checked = True
            elif tentative_g >= neighbor.g:
                continue #better path not found
            
            neighbor.parent = current
            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor.pos, destination.pos)
            neighbor.totalCost = neighbor.g + neighbor.h

def make_path(start, destination):
    current = destination

    while current is not None:
        current.isPath = True
        current = current.parent

def print_grid(start=None, destination=None):
    for y in range(grid_size):
        for x in range(grid_size):
            text = "[bold][white]███"
            if grid[x][y].isObstacle:
                text = "[bold][black]███"
            if grid[x][y].checked:
                text = "[grey]███"
            if grid[x][y].isPath:
                text = "[bold][cyan]███"
            if grid[x][y] == start:
                text = "[bold][green]███"
            if grid[x][y] == destination:
                text = "[bold][red]███"

            if x == grid_size - 1:
                Console().print(text, end="\n")
            else:
                Console().print(text, end="")

def heuristic(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_neighbors(currentPos):
    x, y = currentPos
   
    possible_moves = [
        (x+1, y), (x-1, y), # right, left
        (x, y+1), (x, y-1), # up, down
        (x+1, y+1), (x-1, y-1), # diagonal
        (x+1, y-1), (x-1, y+1), 
    ]

    return [
    grid[newX][newY] for newX, newY in possible_moves
    if newX >= 0 and newX <= grid_size - 1 and newY >= 0 and newY <= grid_size - 1 and not grid[newX][newY].isObstacle
    ]

create_grid()
print_grid()

print("start node: ")
startX = min(max(int(input("input x: ")), 0), grid_size-1)
startY = min(max(int(input("input y: ")), 0), grid_size-1)

start = grid[startX][startY] 
print_grid(start)

print("destination node: ")
destinationX = min(max(int(input("input x: ")), 0), grid_size-1)
destinationY = min(max(int(input("input y: ")), 0), grid_size-1)

destination = grid[destinationX][destinationY]

obstacles = min(max(int(input("input number of obstacles: ")), 0), (grid_size**2) - 2)

add_obstacles(obstacles, start, destination)
print_grid(start, destination)

print("")
print("")
print("")

path = algorithm(start, destination)
print_grid(start, destination)

